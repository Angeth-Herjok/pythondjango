from django import forms
from .models import Cart

class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"
# from django import forms

# class AddToCartForm(forms.Form):
#     quantity = forms.IntegerField(min_value=1)













