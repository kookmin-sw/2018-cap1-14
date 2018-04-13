from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_convertor import WaveConvertor, XmlConvertor

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "hello music seat"

@app.route("/extract", methods=["POST"])
def extract():
    json = request.get_json()
    youtube_url = json["youtubeUrl"]

    youtube = WaveConvertor()
    youtube.get_wave("https://www.youtube.com/watch?v=q3fHXqXYMfA")
    
    notes = []        

    #test code
    notes.append("C4")
    notes.append("D4")
    notes.append("E4")
    notes.append("F4")
    notes.append("G4")
    notes.append("A4")
    notes.append("B4")
    #test code

    xml = XmlConvertor.convert(notes)
    print(xml)

    return jsonify(xml=xml)

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)
