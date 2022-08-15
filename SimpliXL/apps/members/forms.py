
from django import forms
from .models import FileUpload


class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file_url']
