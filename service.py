from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import time
from app.classifier import predict_image
app = Flask(__name__)

@app.route('/classification/predict', methods=['POST'])
def predict():
    # Get image from request
    file = request.files['image']
    
    # Open and process the image
    image = Image.open(file.stream)

    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Convert to numpy array (example preprocessing)
    # img_array = np.array(image)
    
    # Placeholder for your model prediction
    t = time.time()
    prediction = predict_image(image)
    t = time.time() - t
    print("prediction time: ",t)
    return prediction

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)