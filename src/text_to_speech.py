#!/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Text-To-Speech API sample application .
Example usage:
    python synthesize_text.py --text "hello"
    python synthesize_text.py --ssml "<speak>Hello there.</speak>"
"""

import argparse
import os
from concurrent.futures import ThreadPoolExecutor

from config import LanguageConfig
from google.cloud import texttospeech
from googletrans import Translator

config = LanguageConfig()

NUMBER_OF_THREADS = 3
EXECUTOR = ThreadPoolExecutor(NUMBER_OF_THREADS)

TRANSLATOR = Translator()


translated_text = {}

# [START tts_synthesize_text]
def synthesize_text(text, output_file_name):
    input_text = None
    for i, (k, v) in enumerate(config.language_voice_map.items()):
        translated_text[k] = TRANSLATOR.translate(text, dest=k)
        # print('\n\n\n' +k + '---->  { ' + translated_text.get(k).text + ' }')
        input_text = texttospeech.SynthesisInput(text=translated_text.get(k).text)
        EXECUTOR.submit(write_to_audio_file, input_text, v, k, 'female', config.audio_config, output_file_name=output_file_name)

    for i, (k, v) in enumerate(config.language_voice_map_male.items()):
        #'*******MALE VERSION STARTS*******'
        input_text = texttospeech.SynthesisInput(text=translated_text.get(k).text)
        EXECUTOR.submit(write_to_audio_file, input_text, v, k, 'male', config.audio_config_male, output_file_name=output_file_name)


def write_to_audio_file(text, voice, language, gender, audio_config, output_file_name):
    print('Task to write to audio file received.')
    client = texttospeech.TextToSpeechClient()
    response = client.synthesize_speech(
        request={"input": text, "voice": voice, "audio_config": audio_config}
    )
    # The response's audio_content is binary.
    file_output = voice.language_code + '_' + gender + '--' + output_file_name
    directory_path = create_directory(str(output_file_name.strip(".mp3")))
    print('final path of file --> ' + directory_path + '/' + file_output)
    with open(directory_path + '/' + file_output, "wb") as out:
        out.write(response.audio_content)
        print('file-->' + file_output)

def create_directory(directory_name):
    try:
        # create a directory on machine
        os.mkdir(directory_name)
    except OSError as error:
        # if the folder exists 
        pass
    return directory_name

# # [START tts_synthesize_ssml]
# def synthesize_ssml(ssml):
#     """Synthesizes speech from the input string of ssml.
#     Note: ssml must be well-formed according to:
#         https://www.w3.org/TR/speech-synthesis/
#     Example: <speak>Hello there.</speak>
#     """
#     from google.cloud import texttospeech

#     client = texttospeech.TextToSpeechClient()

#     input_text = texttospeech.SynthesisInput(ssml=ssml)

#     # Note: the voice can also be specified by name.
#     # Names of voices can be retrieved with client.list_voices().
#     voice = texttospeech.VoiceSelectionParams(
#         language_code="en-US",
#         name="en-US-Standard-C",
#         ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
#     )

#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3
#     )

#     response = client.synthesize_speech(
#         input=input_text, voice=voice, audio_config=audio_config
#     )

#     # The response's audio_content is binary.
#     with open(output_file, "wb") as out:
#         out.write(response.audio_content)
#         print('Audio content written to file ' + output_file)


# [END tts_synthesize_ssml]
# paragraph = INPUT_CONTENT
banned_tags = ["", "ఉందని", "ఇప్పటికే", "నుంచి", "మరో", "చెందే"]


def split_string(string_text):
    import re
    return re.split("\s|(?<!\d)[,.](?!\d)", string_text)


def sort_frequent_word(paragraph):
    mapping = {}
    for word in split_string(paragraph):
        if (mapping.get(word)):
            mapping[word] += 1
        else:
            mapping[word] = 1
    return {k: v for k, v in sorted(mapping.items(), reverse=True, key=lambda item: item[1])}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    group = parser.add_mutually_exclusive_group(required=True)
    # group.add_argument("--text", help="The text from which to synthesize speech.")
    group.add_argument("--input_file", help="The filename of input text path.")
    parser.add_argument("--output_file", help="The filename of input text path.")
    args = parser.parse_args()

    f = open(args.input_file, 'r')
    input_text_content_list = f.read().split('*****')
    for i,input_text_content in enumerate(input_text_content_list):
        output_file_name = args.output_file + '_audio_' + str(i) + '.mp3'
        synthesize_text(input_text_content, output_file_name=output_file_name)
    
    # list_of_tags = sort_frequent_word(paragraph)
    # [list_of_tags.pop(key) for key in banned_tags]

    # print(list_of_tags)

    # if args.text:
    #     pass
    # else:
    #     synthesize_ssml(args.ssml)
