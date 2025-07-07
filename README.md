# 🖼️ Image Classification API (Flask + PyTorch)

This project is a simple Flask-based REST API for image classification using a trained PyTorch model. You can send an image to the API and receive a predicted class label.

---

## 📁 Project Structure

```

classification Model Deployment/
├── app/
│   ├── classifier.py        # Preprocessing and prediction logic
│   └── models/              # Trained model file(s)
├── service.py               # Flask application
├── test\_endpoints.py        # Automated tests (pytest)
├── test.py                  # Manual API testing (requests)
├── requirements.txt         # List of dependencies
├── Cat\_sample.jpg           # Sample image for testing
└── .venv/                   # Virtual environment (optional)

````

---

## ⚙️ Setup Instructions

### 1. Clone the project

```bash
git clone <your-repo-url>
cd "classification Model Deployment"
````

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available, install manually:
> `pip install flask pillow torch torchvision pytest requests`

---

## 🚀 Running the App

Start the Flask API server:

```bash
python service.py
```

By default, it runs on:

```
http://localhost:5000
```

---

## 🔗 API Endpoints

### `GET /`

Health check for the API.

**Response:**

```json
{
  "message": "Welcome to the Image Classification API!"
}
```

---

### `POST /classification/predict`

Send an image to classify.

**Request:**

* Method: `POST`
* Content-Type: `multipart/form-data`
* Field name: `image`

**Example using `curl`:**

```bash
curl -X POST -F "image=@Cat_sample.jpg" http://localhost:5000/classification/predict
```

**Response:**

```json
{
  "label": "cat",
  "confidence": 0.97
}
```

---

## 🧪 Testing

### ✅ 1. Run unit tests with `pytest`

Tests are in `test_endpoints.py`:

```bash
pytest
```

Tests include:

* Health check (`/`)
* Image classification (`/classification/predict`)
* Handling of missing/invalid images

### ✅ 2. Manual test using `requests`

Use `test.py` to send an image request programmatically.

```bash
python test.py
```

It will output the prediction response in your terminal.

---

## 🔬 Example Model (in `app/classifier.py`)

Make sure `classifier.py`:

* Loads the trained model from `app/models/model.pth`
* Applies preprocessing (resize, normalize, etc.)
* Returns predictions as a dictionary: `{"label": ..., "confidence": ...}`

---

## 🧑‍💻 Author

**Mayar Mostafa Hassan**
AI Engineer | Computer Vision | Model Deployment

---
