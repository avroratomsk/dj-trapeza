from django import forms

class CallbackForm(forms.Form):
  name = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваше имя',
      'class': 'form__controls',
      }
  ))

  phone = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваш номер телефона',
      'class': 'form__controls'
      }
  ))
  
class WriteToUsForm(forms.Form):
  name = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Имя',
      'class': 'callback__input',
      }
  ))

  phone = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваш номер телефона',
      'class': 'callback__input',
      }
  ))
  
  message = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Сообщение',
      'class': 'callback__input',
      }
  ))
  
class ConsultForm(forms.Form):
  name = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Имя',
      'class': 'form__controls',
      }
  ))

  phone = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Телефон',
      'class': 'form__controls',
      }
  ))
  
  data = forms.CharField(widget=forms.TextInput(
    attrs={
      'class': 'form__controls',
      }
  ))
  
  number = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Количество человек',
      'class': 'form__controls',
      }
  ))
  reservation = forms.CharField(widget=forms.TextInput(
    attrs={
      'class': 'form__controls',
      }
  ))

class ContactForm(forms.Form):
  name = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Имя',
      'class': 'form__controls',
      }
  ))

  phone = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Телефон',
      'class': 'form__controls',
      }
  ))

  email = forms.EmailField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Email',
      'class': 'form__controls',
      }
  ))

  message = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Сообщение',
      'class': 'form__controls',
      'rows': 5
      }
  ))
     
class ReviewsForm(forms.Form):
  name = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Имя',
      'class': 'form__controls',
      }
  ))
  
  email = forms.EmailField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Email',
      'class': 'form__controls',
      }
  ))
  rating = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Имя',
      'class': 'form__controls',
      'type':'hidden',
      'id':'form-reviews__rating'
      }
  ))
  message = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Сообщение',
      'class': 'form__controls',
      'rows': 5
      }
  ))
