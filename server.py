from flask import Flask, request
from downloader import download
from transcripter import transcribe
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
    print(tr_data['url'])
    tr = transcribe(url=tr_data['url'])
    tr.transcripter()
    return "Success"