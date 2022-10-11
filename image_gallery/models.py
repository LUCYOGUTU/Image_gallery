from email.mime import image
from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200)
