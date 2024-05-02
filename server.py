from flask import Flask, request
from downloader import download
from transcripter import transcribe
from detector import Detector
from tts import SpeechSynthesizer
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return "st.write('Hello, World')"

@app.route('/downloader', methods=['GET', 'POST'])
def downloader():
    dw_data = request.json
    dw = download(dw_data['url'])
    print(dw_data['chosen_res'])
    response = dw.downloader(dw_data['chosen_res'])
    if response == "error":
        print("no A/V streams (server response !)")
    else:
        print(f'server : video{response}')
    return response

@app.route("/transcripter", methods=['GET', 'POST'])
def transcripter():
    tr_data = request.json
    print(tr_data['url'], tr_data['source_lang'])
    tr = transcribe(url=tr_data['url'], lang_code=tr_data['source_lang'])
    text = tr.transcripter()
    if text == 1:
        return 'Failed'
    else:
        print('\n\nserver\n' + text + '\n\n')
        return text

@app.route("/detector", methods=['GET', 'POST'])
def detector():
    dtr_data = request.json
    print(dtr_data['video_id'])
    tr = Detector(id=dtr_data['video_id'])
    tr.detect_language()
    return "Success"

@app.route("/voiceover", methods=['GET', 'POST'])
def voiceover():
    data = request.json
    print('\n\nI D \n' + data['id'] + '\n\n')
    tts = SpeechSynthesizer(data['id'])
    resp = tts.synthesize_text(data['text'])
    return resp