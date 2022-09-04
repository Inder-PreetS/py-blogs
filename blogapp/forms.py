from .models import *
from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class blogForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    content = CKEditorUploadingWidget()
    slug = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    tag = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=Blog
        fields='__all__'
        exclude=['audio_url', 'audio_status', 'state', 'user']