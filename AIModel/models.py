from django.db import models

class ImageClassifier(models.Model):
    prediction = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
