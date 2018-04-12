from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
  return "hello music seat"

@app.route("/extract", methods=["POST"])
def extract():
  json = request.get_json()
  print(json["youtubeUrl"])
  return jsonify(response="test")

@app.route("/convert-test")
def convert():
  convert_url_to_audio("https://www.youtube.com/watch?v=q3fHXqXYMfA")
  return "test"

if __name__ == "__main__":
  app.run(host="0.0.0.0", threaded=True)
