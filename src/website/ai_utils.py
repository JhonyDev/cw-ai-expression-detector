from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import model_from_json
import cv2
import numpy as np


def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(224, 224))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    # img = img - [123.68, 116.779, 103.939]
    return img


# load an image and predict the class
def run(file):
    print(file)
    print('LOADED IMAGE PATH OF IMAGE')
    print('----------------------------------------------')
    json_file = open('fer.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("fer.h5")
    print("Loaded model from disk")

    WIDTH = 48
    HEIGHT = 48
    x = None
    y = None
    labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

    full_size_image = cv2.imread(file)
    print("Image Loaded")
    gray = cv2.cvtColor(full_size_image, cv2.COLOR_RGB2GRAY)
    face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face.detectMultiScale(gray, 1.3, 10)
    print("FEEDING IMAGE TO MODEL  ")
    # detecting faces
    for (x, y, w, h) in faces:
        print("IMAGES LOOP")
        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        cv2.normalize(cropped_img, cropped_img, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
        cv2.rectangle(full_size_image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        #         predicting the emotion
        yhat = loaded_model.predict(cropped_img)
        cv2.putText(full_size_image, labels[int(np.argmax(yhat))], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0),
                    1, cv2.LINE_AA)
        print("Emotion: " + labels[int(np.argmax(yhat))])
        return labels[int(np.argmax(yhat))]
