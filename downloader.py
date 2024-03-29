# for captions :- vid.captions ( shows all languages in which the captions are avaialable, if any )
# does not work directly, use print(len(vid.streams)) beforehand
#
# for thumbnail :- vid.thumbnail_url
# for title :- vid.title
# for getting transcript :- captions.generate_srt_captions()

from pytube import YouTube
import data as d
# # Create a YouTube object
# yt = YouTube(d.link)

# # Get the available streams for the video
# streams = yt.streams

class download:
    def __init__(this, url):
        this.url = url
        this.yt = YouTube(this.url)
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

    def downloader(this, chosen_res):
        try:
            # Get the streams with a maximum resolution of 720p
            video_stream = this.yt.streams.filter(res=str(chosen_res)).first()
            video_stream.download(output_path='videos')
        except Exception as e:
            print('Error downloading video !')