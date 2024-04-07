import streamlit as st
import requests as rq
import re
from downloader import download
import data as d
error_count = 0

st.title('LINUDIO')
url = st.text_input('Enter *link*: ', placeholder='https://www.youtube.com/watch?v=xvFZjo5PgG0', type="default")

if 'downloaded' not in st.session_state:
    st.session_state['downloaded'] = False

if 'transcribed' not in st.session_state:
    st.session_state['transcribed'] = False

def send_req(endpoint, args):
    response = rq.post(url = f"http://127.0.0.1:5000/{endpoint}", json = args)

try: 
    dw = download(url)
    st.video(url)
    res = sorted((dw.fetch_res()), reverse=True)
    resolutions = set()
    for r in res:
        resolutions.add(str(r) + 'p')
    option = st.selectbox ('Select Resolution: ', resolutions, index = 0)

    if option:
        if not st.session_state['downloaded']: 
            start = st.button("Begin Transcription - ")

            if start:
                try:
                    # st.write(dw.yt.title + '.mp4')
                    progressbar = st.progress(0, text='Download Progress')
                    
                    d.download_response = rq.post(url="http://127.0.0.1:5000/downloader", json = {'chosen_res' : str(option), 'url' : dw.url})
                    st.write('after download')
                    progressbar.progress(50)
                    id = d.download_response
                    st.write(d.download_response.text)
                    progressbar.progress(100)
                    
                    if d.download_response:
                        st.write('updated session')
                        st.session_state['downloaded'] = True
                except Exception as e:
                    st.error("Video couldn't be downloaded")
                    st.write(e)

    if st.session_state['downloaded']:
        title = dw.yt.title
        title = re.sub(r'[^\w\s(){}\[\]<>]', '', title)
        st.write(title)
        
        if not st.session_state['transcribed']:
            transcribe = st.button("Start Transcription - ")
            
            if transcribe:
                trans_resp = rq.post(url="http://127.0.0.1:5000/transcripter", json={'url' : f'video{d.download_response.text}.mp4'})
                
                if trans_resp.text == "Success":
                    st.session_state['transcribed'] = True
                    st.write("Success")
    
    if st.session_state['transcribed']: 
        with open('response.txt', mode='r', encoding= 'utf-8') as f:
                content = f.read()
        st.markdown(content)

except Exception as e:
    st.error('Video not available')
    st.error(e)