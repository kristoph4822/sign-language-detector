from flask import Flask, render_template, request, make_response, jsonify
import cv2
import numpy as np
import datetime
import requests as req
import base64
import model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/upload', methods=['POST'])
def upload():
    img = base64.b64decode(request.data)
    img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_UNCHANGED)
    predictions = model.predict(img)
    predictions = list(filter(lambda x: x.get("probability") > 0.5, predictions))
    return jsonify({"predictions": predictions})
    
if __name__ == '__main__':    
    app.run(debug=True, port=5000)