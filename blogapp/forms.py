from .models import *
from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget

class blogForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model=Blog
        fields='__all__'
        exclude=['audio_url', 'audio_status', 'state', 'user']