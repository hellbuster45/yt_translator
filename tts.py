# import azure.cognitiveservices.speech as speechsdk

# # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
# speech_config = speechsdk.SpeechConfig(subscription='d46b07d512184b839945030e6b17abda', region="centralindia")
# audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# # The neural multilingual voice can speak different languages based on the input text.
# speech_config.speech_synthesis_voice_name='en-US-AvaMultilingualNeural'

# speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# # Get text from the console and synthesize to the default speaker.
# print("Enter some text that you want to speak >")
# text = """अगर यह दिन, मेरी जिंदगी का आखिरी दिन मैं कल सुबह नहीं उठने वाला। फिर भी आज रात को च
# ैंस हूँ। इस काम को करने के लिए कोई भी चीज गंवाने को तैयार। अगर पूरी दुनिया मुझे कहत
# ी है कि मेरी तो किस्मत खराब है, मेरे हाथ की है, तो क्यों मैं अपने हाथ की लकीरों को 
# नहीं बदल सकता? वो दिन दूर नहीं है जब आपके पास सब कुछ होगा, लेकिन फिर भी अपना कुछ भी
#  खोने का डर नहीं होगा।"""

# speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

# if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#     print("Speech synthesized for text [{}]".format(text))
# elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = speech_synthesis_result.cancellation_details
#     print("Speech synthesis canceled: {}".format(cancellation_details.reason))
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         if cancellation_details.error_details:
#             print("Error details: {}".format(cancellation_details.error_details))
#             print("Did you set the speech resource key and region values?")



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