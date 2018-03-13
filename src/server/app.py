from flask import Flask
from src.youtube_url_convertor import convert_url_to_audio

app = Flask(__name__)

@app.route("/")
def index():
  return "hello music seat"

@app.route("/convert-test")
def convert():
  convert_url_to_audio("https://www.youtube.com/watch?v=q3fHXqXYMfA")
  return "test"

if __name__ == "__main__":
  app.run(host="0.0.0.0", threaded=True)
