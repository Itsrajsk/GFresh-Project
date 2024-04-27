from django.contrib import admin
from .models import products

# Register your models here.




class productsAdmin(admin.ModelAdmin):
    list_display =('product_img','product_name','product_price')


admin.site.register(products,productsAdmin)