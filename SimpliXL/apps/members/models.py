from pyexpat import model
from django.db import models
from apps.accounts.models import CustomUser
# from django.contrib.auth import get_user_model

# Create your models here.


class FileUpload(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    file_url = models.FileField(upload_to='uploaded/document/')
    date_created = models.DateTimeField(auto_now_add=True)
