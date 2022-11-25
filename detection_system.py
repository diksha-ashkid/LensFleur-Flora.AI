import cv2
import numpy as np
from keras.models import load_model
import glob
import matplotlib.pyplot as plt
model_finetuned = load_model('model_finetuned.h5')

IMAGE_SIZE = [224, 224]

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


def load_image(filename):
    img = cv2.imread(filename)
    img = cv2.resize(img, (IMAGE_SIZE[0], IMAGE_SIZE[1]) )
    img = img /255
    
    return img

def predict(image):
    probabilities = model_finetuned.predict(np.asarray([image]))[0]
    class_idx = np.argmax(probabilities)
    return class_idx

path ='D:/Computer/Assignments/PlantDisease/Datasets/test/test/'
PList=glob.glob('D:/Computer/Assignments/PlantDisease/Datasets/test/test/*')
for filename in PList:
    img = load_image(str(filename))
    prediction = predict(img)
    print(classes[prediction])
    # cv2.WINDOW_NORMAL
    # cv2.putText(img, classes[prediction], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    plt.imshow(img)
    plt.axis('off')
    plt.title(classes[prediction])
    plt.show()