import streamlit as st
import requests as rq
import re
from downloader import download

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
    if not st.session_state['downloaded']: 
        start = st.button("Begin Transcription - ")

        if start:
            try:
                # st.write(dw.yt.title + '.mp4')
                progressbar = st.progress(0, text='Download Progress')
                
                dw_resp = rq.post(url="http://127.0.0.1:5000/downloader", json = {'chosen_res' : '144p', 'url' : dw.url})
                
                progressbar.progress(50)
                st.write(dw_resp.text)
                progressbar.progress(100)
                
                if dw_resp.text == "Success":
                    st.session_state['downloaded'] = True
            except:
                st.error("Video couldn't be downloaded")

        if st.session_state['downloaded']:
            title = dw.yt.title
            title = re.sub(r'[^\w\s()-[\]{}<>]', '', title)
            st.write(title)
            if not st.session_state['transcribed']:
                transcribe = st.button("Start Transcription - ")
                
                if transcribe:
                    trans_resp = rq.post(url="http://127.0.0.1:5000/transcripter", json={'url' : title + '.mp4'})
                    
                    if trans_resp.text == "Success":
                        st.session_state['transcribed'] = True
                        st.write("Success")
except Exception as e:
    if error_count == 0:
        error_count = 1
    else:
        st.error('Video not available')
        st.error(e)