from distutils.text_file import TextFile
from django.db import models
from django.forms import CharField, ImageField

# Create your models here.


class MainPage(models.Model):
    image = models.ImageField(upload_to='media/uploads')
    title = models.CharField(max_length=400)
    body  = models.TextField()
    about_us_product = models.CharField(max_length=200)
    video = models.FileField(upload_to='media/uploads')

class MainAboutProduct(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)    

