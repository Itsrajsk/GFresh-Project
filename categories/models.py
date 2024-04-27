from django.db import models

# Create your models here.

class categories(models.Model):
    categorie_img = models.ImageField(upload_to="categorie/", max_length=250 , null=True , default = None)
    categorie_name = models.CharField(max_length=50)
    categorie_discount = models.CharField(max_length=100)