from django.db import models
from django_cleanup import cleanup

# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField(upload_to='img/')