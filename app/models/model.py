import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import json

  
def load_model():
    model = models.alexnet(pretrained=True)
    model.eval()

    return model