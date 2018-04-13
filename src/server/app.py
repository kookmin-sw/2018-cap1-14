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
    
    xml = XmlConvertor.convert("test")
    print(xml)

    return jsonify(xml=xml)

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)
