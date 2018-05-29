from flask import Flask
from youtube_convertor import wave_convertor

app = Flask(__name__)

@app.route("/")
def index():
    return "hello music seat"

@app.route("/convert-test")
def convert():
    youtube = WaveConvertor()
    youtube.get_wave("https://www.youtube.com/watch?v=q3fHXqXYMfA")
    return "test"

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)
