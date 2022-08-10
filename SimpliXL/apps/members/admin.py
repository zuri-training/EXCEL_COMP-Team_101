from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.FileUpload)
admin.site.register(models.Profile)