from flask import Flask, request, jsonify
from flask_cors import CORS
from scipy.io import wavfile # get the api
from youtube_convertor import WaveConvertor, XmlConvertor, NoteConvertor

app = Flask(__name__)
CORS(app)

@app.route("/extract", methods=["POST"])
def extract():
    json = request.get_json()
    youtube_url = json["youtubeUrl"]

    youtube = WaveConvertor()
    wave = youtube.get_wave(youtube_url)
    note_convertor = NoteConvertor(wave)
    notes = note_convertor.convert()
    json = jsonify(notes=notes)
    return json

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)
