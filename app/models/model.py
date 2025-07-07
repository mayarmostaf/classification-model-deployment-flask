import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import json


Model = None

def load_model():
    global Model
    if not Model:
        Model = models.alexnet(pretrained=True)
        Model.eval()

    return Model