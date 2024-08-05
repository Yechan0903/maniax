from django import forms
from .models import Upload_Image

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Upload_Image
        fields = ['image']
