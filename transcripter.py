import assemblyai as aai
import data as d

# API key
aai.settings.api_key = d.auth_key

# File URL
# FILE_URL = "videos\jpen.mp4"
FILE_URL = r"videos\LowTierGod Open Verse Challenge meme.mp4"

config = aai.TranscriptionConfig(language_detection=True)
transcriber = aai.Transcriber(config=config)

transcript = transcriber.transcribe(FILE_URL, config=config)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)

with open('response.txt', mode='w', encoding= 'utf-8') as f:
    f.write(transcript.export_subtitles_srt())