from django import forms
from django.db import models
from .models import Fayl
from django.contrib.auth.models import User

class FaylForm(forms.ModelForm):
    muellif=forms.CharField(widget = forms.HiddenInput(), required=False)

    class Meta:
        model=Fayl
        fields=['ad', 'fayl', 'aciqlama']
        labels = {
            "aciqlama": "Açıqlama"
        }
    def save(self, commit=True, user=None):
        obj = super().save(commit=False) # here the object is not commited in db
        obj.muellif = user
        obj.save()
        return obj




