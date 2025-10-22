from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/crystal/audio")
def crystal_audio():
    return send_file("static/audio/crystal_intro.mp3")

if __name__ == "__main__":
    app.run(debug=True, port=9091)
