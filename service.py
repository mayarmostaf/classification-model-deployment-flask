from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import time
from app.classifier import  predict_image, preprocess_image
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Image Classification API!"})


@app.route('/classification/predict', methods=['POST'])
def predict():
    # Get image from request
    file = request.files['image']
    
    # Open and process the image
    image = Image.open(file.stream)

    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Preprocess the image
    image = preprocess_image(image)

    #predict the class
    t = time.time()
    prediction = predict_image(image)
    t = time.time() - t
    print("prediction time: ",t)
    
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)