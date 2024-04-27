from django.db import models

# Create your models here.


class subscribe(models.Model):
    id = models.AutoField(primary_key=True)
    sub_email = models.EmailField(max_length=254)
