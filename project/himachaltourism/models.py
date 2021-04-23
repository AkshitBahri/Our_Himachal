from django.db import models

# Create your models here.

class imageupload(models.Model):

    img=models.ImageField(upload_to='pics')
    msg=models.TextField()


class ims(models.Model):

    img=models.ImageField(upload_to='pics')
    msg=models.TextField()


class contactus(models.Model):

    name=models.CharField(max_length=100)
    message=models.TextField()
