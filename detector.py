import requests
import moviepy.editor as mp
import data as d

class Detector:
    def __init__(this, id):
        this.api_key = d.deepgram_key
        this.url = 'https://api.deepgram.com/v1/listen'
        this.headers = {
            'Authorization': f'Token {d.deepgram_key}',
            'Content-Type': 'audio/wav'
        }
        this.video_id = id
        this.video_url = f'videos\\video{id}.mp4'
        print('in constrcutor detctor')

    def detect_language(this):
        print('hello in function detct')
        # Extract audio from the video file and save it as a WAV file
        audio = mp.VideoFileClip(this.video_url).audio
        audio_file_path = f'audios\\video{this.video_id}.mp3'
        print(f'\n\n{this.video_id}\n')
        print(f'{this.video_url}\n\n')
        audio.write_audiofile(audio_file_path, codec='libmp3lame')

        print('\n\naudio made\n\n')
        # Open the audio file in binary mode and read its content
        with open(audio_file_path, 'rb') as file:
            audio_data = file.read()

        # Create the request with the appropriate data
        response = requests.post(this.url, headers=this.headers, data=audio_data, params={'model': 'nova-2-general', 'detect_language': 'true'})
        print('resquest sent for detecting')

        # Check if the request was successful
        if response.ok:
            print('response done ')
            return response
        else:
            # Print the error message
            print(f"Error: {response.status_code} - {response.text}")
            return 'Failed'