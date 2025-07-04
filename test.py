import requests

# Endpoint URL
url = "http://localhost:5000/classification/predict"

# Image file to upload
image_path = "Cat_November_2010-1a.jpg"

# Additional form data (optional)
data = {
    "user_id": "12345",
    "description": "Sample image upload"
}

# Send POST request with image
with open(image_path, 'rb') as img_file:
    files = {
        'image': ('image.jpg', img_file, 'image/jpeg')
    }
    response = requests.post(url, data=data, files=files)

# Print response
print("Status Code:", response.status_code)
print("Response Body:", response.text)
