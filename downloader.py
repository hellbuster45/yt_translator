# for captions :- vid.captions ( shows all languages in which the captions are avaialable, if any )
# does not work directly, use print(len(vid.streams)) beforehand
#
# for thumbnail :- vid.thumbnail_url
# for title :- vid.title
# for getting transcript :- captions.generate_srt_captions()

from pytube import YouTube
import data as d
import string
import random

class download:
    def __init__(this, url):
        this.url = url
        this.yt = YouTube(this.url, on_progress_callback=this.progress)
        this.streams = this.yt.streams

    def fetch_res(this):
        try:
            # Extract unique resolutions from the video streams
            resolutions = set()
            for stream in this.streams:
                if stream.resolution:
                    resolutions.add(int(stream.resolution[:-1])) # removing 'p' from the resolutions
            return resolutions
        except Exception as e:
            print('Error fetching video information')

    def progress(this, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        print(f"Downloaded: {percentage:.2f}%")

    def generate_random_string(this, length):
        alphanumeric_characters = string.ascii_letters + string.digits
        return ''.join(random.choice(alphanumeric_characters) for _ in range(length))
    
    def downloader(this, chosen_res):
        try:
        #     Get the streams with a maximum resolution of 720p
        
            rand_id = this.generate_random_string(4)
            video_stream = this.streams.filter(only_audio=True).first()
            video_stream.download(output_path='videos', filename=f'video{rand_id}')

            print(f'video{rand_id}')
        except Exception as e:
            print('Error downloading video !')
            print(e)
        return rand_id