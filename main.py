from flask import Flask, Response, render_template
import time
import json
import numpy as np
from asciiVid.convert_ascii import get_frames

app = Flask(__name__)

path = 'asciiVid\\Garp vs Aokiji Full Fight _ One Piece Anime.mp4'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/stream")
def stream():
    def generate():
        frame = get_frames(path)

        for i in frame:
            color , gray = i
            payload = {
                "gray": gray.tolist(),
                "color": color.tolist(),
                #"array3": [10, 20, 30]
            }

            yield f"data: {json.dumps(payload)}\n\n"
            

    return Response(generate(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True, threaded=True)