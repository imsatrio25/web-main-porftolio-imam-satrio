import numpy as np
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from keras.applications import vgg16
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing.image import img_to_array, load_img
from tensorflow.python.keras.backend import set_session
from .predict import process


def predict(request):
    if request.method == "POST":
        #
        # Django image API
        #
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)

        #
        # https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/load_img
        #
        image = load_img(file_url, target_size=(224, 224))
        numpy_array = img_to_array(image)
        image_batch = np.expand_dims(numpy_array, axis=0)
        processed_image = process(image_batch.copy())

        #
        # get the predicted probabilities
        
        #
        # Output/Return data
        return render(request, "index.html", {"predictions": processed_image})

    else:
        return render(request, "index.html")
    
    return render(request, "index.html")

    # if request.method == 'POST':
    #     form = ImageUploadForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         uploaded_image = request.FILES['image']
    #         prediction = process(uploaded_image)
    #         predicted_image = ImageClassifier.objects.filter(prediction=prediction).first()
    #         predicted_image_url = predicted_image.image.url if predicted_image else ''

            
    #         response_data = {
    #                 'prediction': prediction,
    #                 'predicted_image': predicted_image_url,
    #             }

    #         return JsonResponse(response_data)
    # else:
    #     form = ImageUploadForm()
    # return JsonResponse({})