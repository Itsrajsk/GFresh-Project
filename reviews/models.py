from django.db import models

# Create your models here.

class reviews(models.Model):
    reviewer_img = models.ImageField(upload_to="reviewer/", max_length=250 , null=True , default = None)
    reviewer_name = models.CharField(max_length=50)
    reviewer_dec = models.CharField(max_length=500)