from django import forms
from .models import *
from users.models import *

class UploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =('user','image')