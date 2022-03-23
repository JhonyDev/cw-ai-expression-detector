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
    from keras.preprocessing import image
    from keras.models import model_from_json
    import numpy as np
    print('LOADED IMAGE PATH OF IMAGE')
    print('----------------------------------------------')
    json_file = open('C:\\Users\\Jhony Dev\\PycharmProjects\\cw-ai-expression-detector\\fer.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights('C:\\Users\\Jhony Dev\\PycharmProjects\\cw-ai-expression-detector\\fer.h5')
    print("Loaded model from disk")

    WIDTH = 48
    HEIGHT = 48
    x = None
    y = None
    labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

    # full_size_image = cv2.imread('photo.jpg', target_size=(WIDTH, HEIGHT), grayscale=True)
    full_size_image = image.load_img(file, target_size=(WIDTH, HEIGHT), grayscale=True)
    print("Image Loaded")
    full_size_image = image.img_to_array(full_size_image)
    full_size_image = np.expand_dims(full_size_image, axis=0)
    result = loaded_model.predict(full_size_image)
    # print(result)
    print(np.argmax(result))
    print("Emotion: " + labels[int(np.argmax(result))])
    return labels[int(np.argmax(result))]
