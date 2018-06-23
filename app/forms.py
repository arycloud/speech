from django import forms

from . import models


class BaseForm(forms.ModelForm):
    class Meta:
        model = models.BaseModel
        fields = ('textFile', 'gender', 'voice_type', 'pitch', 'speed')
