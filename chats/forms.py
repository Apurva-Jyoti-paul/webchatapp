from django import forms
from .models import gchat,wpgc


class txtform(forms.ModelForm):
    class Meta:
        model=gchat
        fields=('chattxt',)


class groupform(forms.ModelForm):
    class Meta:
        model=wpgc
        fields=('name',)