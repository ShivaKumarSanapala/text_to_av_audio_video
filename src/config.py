from google.cloud import texttospeech


class LanguageConfig:
    def __init__(self):
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=0.9,
            pitch=1.5
        )

        self.audio_config_male = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=0.9,
            pitch=-1
        )

        telugu_voice = texttospeech.VoiceSelectionParams(
            language_code="te-IN",
            name="te-IN-Standard-A",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )

        hindi_voice = texttospeech.VoiceSelectionParams(
            language_code="hi-IN",
            name="hi-IN-Wavenet-A",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )

        tamil_voice = texttospeech.VoiceSelectionParams(
            language_code="ta-IN",
            name="ta-IN-Standard-A",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )

        kannada_voice = texttospeech.VoiceSelectionParams(
            language_code="kn-IN",
            name="kn-IN-Standard-A",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )

        bengali_voice = texttospeech.VoiceSelectionParams(
            language_code="bn-IN",
            name="bn-IN-Standard-A",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )

        english_voice = texttospeech.VoiceSelectionParams(
            language_code="en-IN",
            name="en-IN-Standard-A",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )

        # Male voice config

        male_telugu_voice = texttospeech.VoiceSelectionParams(
            language_code="te-IN",
            name="te-IN-Standard-B",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )

        male_hindi_voice = texttospeech.VoiceSelectionParams(
            language_code="hi-IN",
            name="hi-IN-Wavenet-B",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )

        male_tamil_voice = texttospeech.VoiceSelectionParams(
            language_code="ta-IN",
            name="ta-IN-Standard-B",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )

        male_kannada_voice = texttospeech.VoiceSelectionParams(
            language_code="kn-IN",
            name="kn-IN-Standard-B",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )

        male_bengali_voice = texttospeech.VoiceSelectionParams(
            language_code="bn-IN",
            name="bn-IN-Standard-B",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )

        male_english_voice = texttospeech.VoiceSelectionParams(
            language_code="en-IN",
            name="en-IN-Standard-B",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )

        self.language_voice_map = {
            # 'te': telugu_voice,
            'hi': hindi_voice,
            # 'ta': tamil_voice,
            # 'kn': kannada_voice,
            # 'bn': bengali_voice,
            'en': english_voice
        }

        self.language_voice_map_male = {
            # 'te': male_telugu_voice,
            'hi': male_hindi_voice,
            # 'ta': male_tamil_voice,
            # 'kn': male_kannada_voice,
            # 'bn': male_bengali_voice,
            'en': male_english_voice
        }

