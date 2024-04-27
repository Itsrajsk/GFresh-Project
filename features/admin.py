from django.contrib import admin
from .models import features

# Register your models here.


class featuresAdmin(admin.ModelAdmin):
    list_display =('feature_img','feature_name','feature_dec')


admin.site.register(features,featuresAdmin)