from django import forms
from .models import Category


class CategoryAddForm(forms.Form):
     name = forms.CharField()
    # class Meta:
    #     model = Category
    #     widgets = {
    #          'name': forms.TextInput(attrs={'class': 'form-control'}),
    #     }


