import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import json

from app.models.model import load_model


imagenet_labels = {
    0: "tench", 1: "goldfish", 2: "great_white_shark", 3: "tiger_shark",
    4: "hammerhead", 5: "electric_ray", 281: "tabby_cat", 282: "tiger_cat",
    283: "persian_cat", 284: "siamese_cat", 285: "egyptian_cat", 
    207: "golden_retriever", 208: "labrador_retriever", 209: "cocker_spaniel",
    151: "chihuahua", 152: "japanese_spaniel", 153: "maltese_dog",
    945: "strawberry", 946: "orange", 947: "lemon", 948: "fig",
    949: "pineapple", 950: "banana", 951: "jackfruit", 952: "custard_apple",
    404: "airliner", 407: "ambulance", 468: "cab", 511: "convertible",
    817: "sports_car", 875: "trolleybus", 656: "minivan", 751: "racer",
    924: "guacamole", 925: "consomme", 926: "hot_pot", 927: "trifle",
    928: "ice_cream", 929: "ice_lolly", 930: "french_loaf", 931: "bagel"
}

def preprocess_image(image):
    pass
def predict_image(image):
   
 
    dict_pred = {"class":'class_name',"score":'confidence'}
    
    return dict_pred