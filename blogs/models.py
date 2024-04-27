from django.db import models

# Create your models here.

class blogs(models.Model):
    blog_img = models.ImageField(upload_to="blog/", max_length=250 , null=True , default = None)
    blog_author = models.CharField(max_length=100)
    blog_date = models.DateField()
    blog_title = models.CharField(max_length=100)
    blog_dec = models.CharField(max_length=500)
