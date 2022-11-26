from flask import Flask, render_template, request
from keras.applications import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.utils import load_img
from keras.utils import img_to_array
from keras.models import load_model
from keras.layers import Lambda
import keras.applications.mobilenet_v2 as mobilenetv2
import numpy as np
import pandas as pd
import exif #API to extract metadata
from exif import Image as im
from geopy.geocoders import Nominatim #geolocation services
import wikipedia #use wikipedia api
import cv2

app = Flask(__name__)
classes=['Apple scab', 'Apple Black rot', 'Cedar apple rust', 
         'Apple healthy', 'Blueberry healthy', 
         'Cherry Powdery mildew', 'Cherry healthy', 
         'Corn Cercospora leaf spot', 'Corn Common rust', 
         'Corn Northern Leaf Blight', 'Corn healthy', 
         'Grape Black rot', 'Grape Black Measles', 
         'Grape Leaf blight', 'Grape healthy', 
         'Orange Haunglongbing', 'Peach Bacterial spot', 
         'Peach healthy', 'Bell Peppers Bacterial spot', 'Bell Peppers healthy', 
         'Potato Early blight', 'Potato Late blight', 'Potato healthy', 
         'Raspberry healthy', 'Soybean healthy', 'Squash Powdery mildew', 
         'Strawberry Leaf scorch', 'Strawberry healthy', 'Tomato Bacterial spot', 
         'Tomato Early blight', 'Tomato Late blight', 'Tomato Leaf Mold', 
         'Tomato Septoria leaf spot', 'Tomato Spider mites', 
         'Tomato Target Spot', 'Tomato Yellow Leaf Curl Virus', 
         'Tomato mosaic virus', 'Tomato healthy']
model = load_model("C:/Users/aakas/Downloads/model_finetuned.h5")
info = pd.read_csv("C:/Users/aakas/Desktop/programs/NNs/dict.csv")
@app.route('/', methods = ['GET'])
def hello_world():
    return render_template('index1.html')
@app.route('/', methods = ['POST'])
def predict():
    # Get the data from the POST request.
    image = request.files['image']
    # Make prediction using model loaded from disk as per the data.
    image_path = image.filename
    image.save(image_path)
    with open(image_path, 'rb') as src:
        copy = im(src)
    
    my_image = cv2.imread(image_path)
    my_image = cv2.resize(my_image, (224, 224) )
    my_image = my_image /255
    probabilities = model.predict(np.asarray([my_image]))[0]
    class_idx = np.argmax(probabilities)
    prediction = classes[class_idx]
    
    #Geolocation Services
    geocoder = Nominatim(user_agent = 'Flora')
    if copy.has_exif:    
        TheDegreeValue, TheMinuteValue, TheSecondValue = copy.gps_latitude
        TheLatitudeValue=TheDegreeValue+(TheMinuteValue/60)+(TheSecondValue/3600)
        TheDegreeValue, TheMinuteValue, TheSecondValue = copy.gps_longitude
        TheLongitudeValue=TheDegreeValue+(TheMinuteValue/60)+(TheSecondValue/3600)
        coord = (TheLatitudeValue, TheLongitudeValue)
        geolocation= geocoder.reverse(coord)
    else:
        geolocation = "No GPS Data"
    q = "info"
    return render_template('results1.html', prediction=prediction, geolocation=geolocation)
if __name__ == '__main__':
    app.run(port = 3000, debug=True)
