import azure.cognitiveservices.speech as speechsdk

class SpeechSynthesizer:
    def __init__(this, id):
        this.id = id
        speech_config = speechsdk.SpeechConfig(subscription='d46b07d512184b839945030e6b17abda', region='centralindia')
        audio_config = speechsdk.audio.AudioOutputConfig(filename = f'voiceovers\\voiceover{id}.wav')
        speech_config.speech_synthesis_voice_name = 'en-US-AvaMultilingualNeural'
        this.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    def synthesize_text(this, text):
        print('\n\n' + text + '\n\n')
        speech_synthesis_result = this.speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
            return "Success"
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
            return 1