from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from shop.models import Categories, Day, Product

# class ProductForm(forms.ModelForm):
#   # description = forms.CharField(label="Полное описание товара", required=False, widget=CKEditorUploadingWidget())
#   class Meta:
#     model = Product
#     fields = (
#       "name", 
#       "short_description",
#       "description",
#       "meta_h1",
#       "meta_title",
#       "meta_description",
#       "meta_keywords",
#       "slug",
#       "price",
#       "discount",
#       "quantity",
#       "category",
#       "day",
#       "subsidiary",
#       "weight",
#       )

class ProductForm(forms.ModelForm):
    """ Form, отвечает за создание товара и редактирование товара"""
    # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'short_description',
            'description',
            'meta_h1',
            'meta_title',
            'meta_description',
            'meta_keywords',
            'image',
            'price',
            'discount',
            'quantity',
            'category',
            'day',
            'subsidiary',
            'image',
            'weight',
            'calories',
            'proteins',
            'fats',
            'carbonhydrates',
            'status',
        ]
        labels = {
            'name': 'Название блюда',
            'slug':'URL',
            'short_description':'Короткое описание',
            'description':'Полное описание',
            'meta_h1':'Заголвок первого уровня',
            'meta_title':'Meta title',
            'meta_description':'Мета description',
            'meta_keywords':'Meta keywords',
            'image':'Изображение',
            'price':'Цена',
            'discount':'Скидка в (%)',
            'quantity':'Количество',
            'category':'Категория',
            'day':'В какой день готовят',
            'subsidiary':'В каком из филлиалов',
            'image': 'Превью изображения',
            'weight':'Грамовка',
            'calories': 'Каллорийность',
            'proteins': 'Белки',
            'fats': 'Жиры',
            'carbonhydrates': 'Углеводы',
            'status': 'Статус публикации'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form__controls',
                "id":"name"
                # 'placeholder': 'Название товара',
                
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form__controls',
                # 'placeholder': 'Короткое описание товара',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form__controls',
                # 'placeholder': 'Короткое описание товара',
            }),
            'meta_h1': forms.TextInput(attrs={
                'class': 'form__controls',
                # 'placeholder': 'h1',
            }),
            'meta_title': forms.TextInput(attrs={
                'class': 'form__controls',
                # 'placeholder': 'Мета заголовок',
            }),
            'meta_description': forms.TextInput(attrs={
                'class': 'form__controls',
                # 'placeholder': 'Мета описание',
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form__controls',
                # 'placeholder': 'Ключевые слова',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form__controls',
                # 'placeholder': 'Цена (с учетом скидки)',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form__controls',
                # 'placeholder': 'Количество',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form__controls',
                "id": "slug"
                # 'placeholder': 'SEO URL',
            }),
            'category': forms.Select(attrs={
                'class': 'form__controls', 
                # 'placeholder': 'Категория',
            }),
            'day': forms.Select(attrs={
                'class': 'form__controls',
                # 'placeholder': 'День приготовления',
            }),
            # 'subsidiary': forms.Select(attrs={
            #     'class': 'form__controls',
            #     'placeholder': 'Филлиал',
            #     'multiply': True
            # }),
            'weight': forms.TextInput(attrs={
                'class': 'form__controls',
                # 'placeholder': 'Грамовка',
            }),
            'discount': forms.TextInput(attrs={
                'class': 'form__controls',
                # 'placeholder': 'Скидка',
            }),
            'image': forms.FileInput(attrs={
                'class': 'submit-file',
                'accept': 'image/*'
            }),
            'calories': forms.TextInput(attrs={
                'class': "form__controls",
                # 'placeholder': 'Колорийность'
            }),
            'proteins': forms.TextInput(attrs={
                'class': "form__controls",
                # 'placeholder': 'Белки'
            }),
            'fats': forms.TextInput(attrs={
                'class': "form__controls",
                # 'placeholder': 'Жиры'
            }),
            'carbonhydrates': forms.TextInput(attrs={
                'class': "form__controls",
                # 'placeholder': 'Углеводы'
            }),
            # 'status': forms.CheckboxInput(attrs={
            #     'class': "form__controls-checkbox",
            #     'placeholder': 'Белки'
            # })
        }
   
class CategoryForm(forms.ModelForm):
  class Meta:
    model = Categories
    fields = [
      "name",
      "slug",
      "image",
      "meta_h1",
      "meta_title",
      "meta_description",
      "meta_keywords"
    ]
    labels = {
      "name": "Назване категории",
      "slug": "URL",
      "image": "Изображение",
      "meta_h1": "Заголовок H1",
      "meta_title": "Meta заголовок",
      "meta_description": "Meta описание",
      "meta_keyword": "Meta keywords",
    }
    widgets = {
      "name": forms.TextInput(attrs={
          "class": "form__controls",
          "id":"name"
          # "placeholder": "Название  категории"
      }),
      "slug": forms.TextInput(attrs={
        "class":"form__controls",
        "id": "slug"
        # "placeholder": "Название категори"
      }),
      'image': forms.FileInput(attrs={
          'class': 'submit-file',
          'accept': 'image/*'
      }),
      "meta_h1": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Заголовок H1"
      }),
      "meta_title": forms.TextInput(attrs={
        "class":"form__controls meta_field",
        "id": "meta_title"
        # "placeholder": "Meta заголовок"
      }),
      "meta_description": forms.Textarea(attrs={
        "class":"form__controls meta_field",
        # "placeholder": "Meta Описание",
        "rows": "5"
      }),
      "meta_keywords": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Meta keywords"
      }),  
    }
    
class DayForm(forms.ModelForm):
  class Meta:
    model = Day
    fields = [
      "name",
      "slug"
    ]
    labels = {
      "name": "Назване категории",
      "slug": "URL",
    }
    widgets = {
      "name": forms.TextInput(attrs={
          "class": "form__controls",
          "id":"name"
          # "placeholder": "Название  категории"
      }),
      "slug": forms.TextInput(attrs={
        "class":"form__controls",
        "id": "slug"
        # "placeholder": "Название категори"
      })
    }