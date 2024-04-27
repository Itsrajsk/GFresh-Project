from django.contrib import admin

from .models import subscribe

# Register your models here.


class subscribeAdmin(admin.ModelAdmin):
    list_display =('id','sub_email')
    

admin.site.register(subscribe,subscribeAdmin)
