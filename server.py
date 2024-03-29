from flask import Flask, request
from downloader import download
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return "st.write('Hello, World')"

@app.route('/downloader', methods=['GET', 'POST'])
def downloader():
    data = request.json
    dw = download(data['url'])
    print(data['chosen_res'])
    dw.downloader(data['chosen_res'])
    return 'Video Downloaded !!'