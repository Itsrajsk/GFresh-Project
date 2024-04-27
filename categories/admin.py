from django.contrib import admin

from .models import categories

# Register your models here.


class categoriesAdmin(admin.ModelAdmin):
    list_display =('categorie_img','categorie_name','categorie_discount')


admin.site.register(categories,categoriesAdmin)
