import streamlit as st
import data as d
from downloader import download

st.title('Hello niggas')
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
        dw.downloader(option)

except Exception as e:
    st.error('Video not available :(')
