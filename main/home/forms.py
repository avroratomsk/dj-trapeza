from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from home.models import HomeTemplate
from shop.models import Category, Day, Product, Branch

class CallbackForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form__controls', 'placeholder': 'Имя'}))
    phone = forms.CharField(label='Телефон',widget=forms.TextInput(attrs={'class': 'form__controls', 'placeholder': 'Телефон'}))
   
