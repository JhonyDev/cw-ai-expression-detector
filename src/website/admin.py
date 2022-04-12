from django.contrib import admin
from .models import ScanImage, Session


class ImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'image_url', 'created_on']


admin.site.register(ScanImage, ImageAdmin)
admin.site.register(Session)
