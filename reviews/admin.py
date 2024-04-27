from django.contrib import admin

from .models import reviews

# Register your models here.


class reviewsAdmin(admin.ModelAdmin):
    list_display =('reviewer_img','reviewer_name','reviewer_dec')


admin.site.register(reviews,reviewsAdmin)
