import pytest
from io import BytesIO
from PIL import Image
from service import app  # import your Flask app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the Image Classification API!"}


def test_predict_endpoint(client):
    # Create a dummy RGB image
    image = Image.new('RGB', (224, 224), color='red')
    img_io = BytesIO()
    image.save(img_io, 'JPEG')
    img_io.seek(0)

    data = {
        'image': (img_io, 'Cat-sample.jpg')
    }

    response = client.post('/classification/predict', content_type='multipart/form-data', data=data)
    assert response.status_code == 200

    prediction = response.get_json()
    assert isinstance(prediction, dict)
    assert 'label' in prediction or 'class' in prediction  # depends on your `predict_image` output
