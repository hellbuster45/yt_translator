import streamlit as st
import data as d
import requests as rq
from downloader import download

st.title('LINUDIO')
url = st.text_input('Enter *link*: ')

try: 
    dw = download(url)
    res = sorted((dw.fetch_res()), reverse=True)
    resolutions = set()
    for r in res:
        resolutions.add(str(r) + 'p')
    option = st.selectbox ('Select Resolution: ', resolutions, index = 0)
    if option:
        start = st.button("Begin Transcription - ")
    if start:
        st.write("hi")

        try:
            progressbar = st.progress(0)
            response = rq.post(url="http://127.0.0.1:5000/downloader", json={'chosen_res' : option, 'url' : dw.url})
            progressbar.progress(50)
            st.write(response.text)
            progressbar.progress(100)
        except:
            st.error("Video couldn't be downloaded")
        # dw.downloader(option)
except Exception as e:
    st.error('Video not available :(')