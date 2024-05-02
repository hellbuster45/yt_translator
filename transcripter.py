import assemblyai as aai
import data as d

class transcribe:
    def __init__(this, url, lang_code):
        # API key
        aai.settings.api_key = d.auth_key
        
        this.file_url = 'videos/' + url
        this.lang_code = lang_code
        this.config = aai.TranscriptionConfig(language_code=this.lang_code, speech_model=aai.SpeechModel.best)
        this.transcriber = aai.Transcriber(config=this.config)

    def transcripter(this):
        transcript = this.transcriber.transcribe(this.file_url, config=this.config)

        if transcript.status == aai.TranscriptStatus.error:
            print(transcript.error)
            return 1
        else:
            print(transcript.text)
            with open('response.txt', mode='w', encoding= 'utf-8') as f:
                f.write(transcript.export_subtitles_srt())
            return transcript.text