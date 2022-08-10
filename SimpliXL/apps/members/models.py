from django.db import models
from apps.accounts.models import CustomUser
from django.core.validators import FileExtensionValidator
from .validators import file_size_limiter

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images')
    location = models.CharField(max_length=100, blank=True)

  #
class FileUpload(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    file_url = models.FileField(
        upload_to='uploaded/document/', validators=[FileExtensionValidator(['csv', 'xlsx', 'xls'], 'Only csv, xlsx, xls files are allowed'), file_size_limiter])
    file_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)


class EditedFileUpload(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    file_url = models.FileField()
    file_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
