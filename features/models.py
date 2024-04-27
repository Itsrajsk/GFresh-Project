from django.db import models

# Create your models here.

class features(models.Model):
    feature_img = models.ImageField(upload_to="feature/", max_length=250 , null=True , default = None)
    feature_name = models.CharField(max_length=50)
    feature_dec = models.CharField(max_length=100)
    
