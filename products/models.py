from django.db import models

# Create your models here.

class products(models.Model):
    product_img = models.ImageField(upload_to="product/", max_length=250 , null=True , default = None)
    product_name = models.CharField(max_length=50)
    product_price = models.CharField(max_length=20)


