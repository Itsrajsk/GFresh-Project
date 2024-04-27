from django.contrib import admin

from .models import blogs

# Register your models here.


class blogsAdmin(admin.ModelAdmin):
    list_display =('blog_img','blog_author','blog_date','blog_title','blog_dec')


admin.site.register(blogs,blogsAdmin)
