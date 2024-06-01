import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model
from io import BytesIO
from .models import ImageClassifier

def process(uploaded_file):
    model = load_model('model/handAI.h5')

    img_path = BytesIO(uploaded_file.read())

    img = image.load_img(img_path, target_size=(100, 150))
    img_array = image.img_to_array(img)
    img_array = img_array * (1/255)
    img_array = tf.expand_dims(img_array, axis=0)
    img_input = tf.reshape(img_array, shape=[1, 100, 150, 3])

    predictions = model.predict(img_input)
    predicted_class_index = np.argmax(predictions)

    if predicted_class_index == 0:
        predicted_class = 'Paper'
    elif predicted_class_index == 1:
        predicted_class = 'Rock'
    else:
        predicted_class = 'Scissors'
    


    predicted_image = ImageClassifier(prediction=predicted_class, image=uploaded_file)
    predicted_image.save()

    return predicted_class