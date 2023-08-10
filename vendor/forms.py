from django import forms
from .models import Vender

class VenderForm(forms.ModelForm):
    class Meta:
        model = Vender
        fields = "__all__"