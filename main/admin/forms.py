from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from home.models import AboutTemplate, BaseSettings, Gallery, HomeTemplate, Stock, StockSettings, Vacancy
from blog.models import BlogSettings, Post
from news.models import News, NewsSettings
from service.models import Banket, PominalnyeObed, Service, ServiceCategory, ServicePage, ServiceProduct
from reviews.models import Reviews
from shop.models import Category, Day, Product, Branch, ShopSettings

class UploadFileForm(forms.Form):
    file = forms.FileField()

class GlobalSettingsForm(forms.ModelForm):
  """ Form, глобальные и общие настройки сайта(лого, телефон, email)"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  class Meta:
    model = BaseSettings
    fields = [
        'logo',
        'email',
        'instagram',
        'telegram',
        'vk',
        'viber',
        'phone_whatsapp',
        'meta_h1',
        'meta_title',
        'meta_description',
        'meta_keywords',
    ]
    labels = {
        'logo': 'Логотип',
        'email': 'Email',
        'meta_h1':'Заголвок первого уровня',
        'meta_title':'Meta title',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
        'email': forms.EmailInput(attrs={
            'class': 'form__controls'
        }),
        'meta_h1': forms.TextInput(attrs={
            'class': 'form__controls'
        }),
        'meta_title': forms.TextInput(attrs={
            'class': 'form__controls'
        }),
        'meta_description': forms.TextInput(attrs={
            'class': 'form__controls'
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': 'form__controls'
        }),
        'instagram': forms.TextInput(attrs={
          'class': 'form__controls'
        }),
        'telegram': forms.TextInput(attrs={
          'class': 'form__controls'
        }),
        'vk': forms.TextInput(attrs={
          'class': 'form__controls'  
        }),
        'viber': forms.TextInput(attrs={
          'class': 'form__controls' 
        }),
        'phone_whatsapp': forms.TextInput(attrs={
          'class': 'form__controls'
        }),
    }
    
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
            'price_two',
            'discount',
            'quantity',
            'category',
            'day',
            'branch',
            'image',
            'weight',
            'weight_two',
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
            'branch':'В каком из филлиалов',
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
            'branch': forms.CheckboxSelectMultiple,
            'short_description': forms.Textarea(attrs={
                'class': 'form__controls',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form__controls'
            }),
            'meta_h1': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'day': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_title': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_description': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'price_two': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form__controls',
                "id": "slug"
            }),
            'category': forms.Select(attrs={
                'class': 'form__controls', 
            }),
            'weight': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'weight_two': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'discount': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'image': forms.FileInput(attrs={
                'class': 'submit-file',
                'accept': 'image/*'
            }),
            'calories': forms.TextInput(attrs={
                'class': "form__controls",
            }),
            'proteins': forms.TextInput(attrs={
                'class': "form__controls",
            }),
            'fats': forms.TextInput(attrs={
                'class': "form__controls",
            }),
            'carbonhydrates': forms.TextInput(attrs={
                'class': "form__controls",
            })
        }
        
class VacancyForm(forms.ModelForm):
    """ Form, отвечает за создание товара и редактирование товара"""
    # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Vacancy
        fields = [
            'name',
            'slug',
            'description',
            'meta_h1',
            'meta_title',
            'meta_description',
            'meta_keywords',
            'price',
            'status',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form__controls',
                "id":"name"
                # 'placeholder': 'Название товара',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form__controls'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'slug': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'meta_h1': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'meta_title': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'meta_description': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'meta_keywords': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
        }

class BlogPage(forms.ModelForm):
  class Meta:
    model = BlogSettings
    fields = [
      "meta_h1",
      "meta_title",
      "meta_description",
      "meta_keywords",
      "image",
      "text"
    ]
    labels = {
        'text': 'Описание статьи',
        'meta_h1': "Заголовок H1",
        'meta_title': "Meta-title",
        'meta_description': 'Meta-description',
        'meta_keywords': "Meta-keywords",
        'image': "Баннер",
        'text': "Текст страницы",
    }
    
    widgets = {
        'text': forms.Textarea(attrs={
            'class': 'form__controls'
        }),
        'meta_h1': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_title': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_description': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
    }
    
class NewsPage(forms.ModelForm):
  class Meta:
    model = NewsSettings
    fields = [
      "meta_h1",
      "meta_title",
      "meta_description",
      "meta_keywords",
      "image",
      "text"
    ]
    labels = {
        'text': 'Описание статьи',
        'meta_h1': "Заголовок H1",
        'meta_title': "Meta-title",
        'meta_description': 'Meta-description',
        'meta_keywords': "Meta-keywords",
        'image': "Баннер",
        'text': "Текст страницы",
    }
    
    widgets = {
        'text': forms.Textarea(attrs={
            'class': 'form__controls'
        }),
        'meta_h1': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_title': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_description': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': 'form__controls',
        })
    }    
    
class StockPage(forms.ModelForm):
  class Meta:
    model = StockSettings
    fields = [
      "meta_h1",
      "meta_title",
      "meta_description",
      "meta_keywords",
      "image",
      "text"
    ]
    labels = {
        'text': 'Описание статьи',
        'meta_h1': "Заголовок H1",
        'meta_title': "Meta-title",
        'meta_description': 'Meta-description',
        'meta_keywords': "Meta-keywords",
        'image': "Баннер",
        'text': "Текст страницы",
    }
    
    widgets = {
        'text': forms.Textarea(attrs={
            'class': 'form__controls'
        }),
        'meta_h1': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_title': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_description': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': 'form__controls',
        })
    }    


class PostForm(forms.ModelForm):
  """ Form, отвечает за создание товара и редактирование товара"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Post
    fields = [
        'name',
        'slug',
        'text',
        'meta_h1',
        'meta_title',
        'meta_description',
        'meta_keywords',
        'image',
        'category',
        'status',
    ]
    labels = {
        'name': "Название статьи",
        'slug': 'URL',
        'text': 'Описание статьи',
        'meta_h1': "Заголовок H1",
        'meta_title': "Meta-title",
        'meta_description': 'Meta-description',
        'meta_keywords': "Meta-keywords",
        'image': "Изображение поста",
        'category': "Категория",
        'status': "Статус публикации",
    }
    widgets = {
        'name': forms.TextInput(attrs={
            'class': 'form__controls',
            "id":"name"
        }),
        'text': forms.Textarea(attrs={
            'class': 'form__controls'
        }),
        'meta_h1': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_title': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_description': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'slug': forms.TextInput(attrs={
            'class': 'form__controls',
            "id": "slug"
        }),
        'category': forms.Select(attrs={
            'class': 'form__controls', 
        }),
        'image': forms.FileInput(attrs={
            'class': 'submit-file',
            'accept': 'image/*'
        })
    }
    
class NewsForm(forms.ModelForm):
  """ Form, отвечает за создание товара и редактирование товара"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = News
    fields = [
        'name',
        'slug',
        'text',
        'meta_h1',
        'meta_title',
        'meta_description',
        'meta_keywords',
        'image',
        'status',
    ]
    labels = {
        'name': "Название",
        'slug': 'URL',
        'text': 'Описание',
        'meta_h1': "Заголовок H1",
        'meta_title': "Meta-title",
        'meta_description': 'Meta-description',
        'meta_keywords': "Meta-keywords",
        'image': "Изображение ноости",
        'status': "Статус публикации",
    }
    widgets = {
        'name': forms.TextInput(attrs={
            'class': 'form__controls',
            "id":"name"
        }),
        'text': forms.Textarea(attrs={
            'class': 'form__controls'
        }),
        'meta_h1': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_title': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_description': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'slug': forms.TextInput(attrs={
            'class': 'form__controls',
            "id": "slug"
        }),
        'image': forms.FileInput(attrs={
            'class': 'submit-file',
            'accept': 'image/*'
        })
    }
   
class CategoryForm(forms.ModelForm):
  """ Form, отвечает за создание категорий и редактирование категорий"""
  class Meta:
    model = Category
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
  """ Form, отвечает за создание дней и редактирование дней"""
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
    
class FillialForm(forms.ModelForm):
  """ Form, отвечает за добавление филлиала и редактирование филлиала"""
  class Meta:
    model = Branch
    fields = [
      "name",
      "address_fillial",
      "phone",
      "time_work",
      "weekend",
      "number_seats",
      "hall_rental",
      "hall_rental_hollyday",
      "scheme_payment",
      "map_code",
      "image",
      "slug"
    ]
    labels = {
      "name": "Название филлиала",
      "address_fillial": "Адрес филлиала",
      "phone": "Номер телефона",
      "time_work": "Режим работы",
      "weekend": "Выходные дни",
      "number_seats": "Количество посадочных мест",
      "hall_rental": "Аренда зала",
      "hall_rental_hollyday": "Аренда зала в праздники",
      "scheme_payment": "Схема оплаты",
      "map_code": "Код карты",
      "image": "Фотография зала",
      "slug": "URL",
    }
    widgets = {
      "name": forms.TextInput(attrs={
          "class": "form__controls",
          "id":"name"
      }),
      "address_fillial": forms.TextInput(attrs={
          "class": "form__controls",
          "id":"name",
          "placeholder": "г.Томск, ул.Ленина 111"
      }),
      "phone": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "time_work": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "weekend": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "number_seats": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "hall_rental": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "hall_rental_hollyday": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "scheme_payment": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "map_code": forms.Textarea(attrs={
          "class": "form__controls",
      }),
      "slug": forms.TextInput(attrs={
        "class":"form__controls",
        "id": "slug"
      })
    }
    
class HomeTemplateForm(forms.ModelForm):
  """ Form, редактирование главной страницы"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
      model = HomeTemplate
      fields = [
          'banner',
          'meta_h1',
          'untitle',
          'left_text',
          'right_text',
          'callback_image',
          'callback_text',
          'meta_title',
          'meta_description',
          'meta_keywords',
          'about_text',
          'about_image'
      ]
      labels = {
          'banner': 'Изображение банера',
          'meta_h1':'Заголвок первого уровня',
          'meta_title':'Meta title',
          'untitle': 'Надзаголовок',
          'meta_description':'Мета description',
          'meta_keywords':'Meta keywords',
          'about_text':'Текст о нас',
          'about_image':'Изображение о нас'
      }
      widgets = {
          'name': forms.TextInput(attrs={
              'class': 'form__controls'
          }),
          'meta_h1': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'untitle': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'left_text': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
          }),
          'right_text': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
          }),
          'callback_text': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
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
          }),
          'about_text': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 5
          }),
      }
      
class PominalnyeForm(forms.ModelForm):
  """ Form, редактирование Поминальные обеды страницы"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
      model = PominalnyeObed
      fields = [
          'title',
          'subtitle',
          'left_text',
          'right_text',
          'first_text_title',
          'first_text_text',
          'second_text_title',
          'second_text_text',
          'meta_h1',
          'meta_title',
          'meta_description',
          'meta_keywords',
      ]
      widgets = {
          'title': forms.TextInput(attrs={
              'class': 'form__controls'
          }),
          'meta_h1': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'subtitle': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
          }),
          'left_text': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
          }),
          'right_text': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
          }),
          'first_text_title': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'first_text_text': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
          }),
          'second_text_title': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'second_text_text': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
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
          })
      }
      
class BanketForm(forms.ModelForm):
  """ Form, редактирование Поминальные обеды страницы"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
      model = Banket
      fields = [
          'title',
          'subtitle',
          'left_text',
          'text_one',
          'text_two',
          'text_three',
          'text_four',
          'meta_h1',
          'meta_title',
          'meta_description',
          'meta_keywords',
      ]
      widgets = {
          'title': forms.TextInput(attrs={
              'class': 'form__controls'
          }),
          'meta_h1': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'subtitle': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
          }),
          'left_text': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
          }),
          'text_one': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
          }),
          'text_two': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
          }),
          'text_three': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
          }),
          'text_four': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 15
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
          })
      }
      
class AboutTemplateForm(forms.ModelForm):
  """ Form, редактирование главной страницы"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
      model = AboutTemplate
      fields = [
          'banner',
          'meta_h1',
          'meta_title',
          'meta_description',
          'meta_keywords',
          'about_text',
          'about_image'
      ]
      labels = {
          'banner': 'Изображение банера',
          'meta_h1':'Заголвок первого уровня',
          'meta_title':'Meta title',
          'meta_description':'Мета description',
          'meta_keywords':'Meta keywords',
          'about_text':'Текст о нас',
          'about_image':'Изображение о нас'
      }
      widgets = {
          'name': forms.TextInput(attrs={
              'class': 'form__controls'
          }),
          'meta_h1': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_title': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_description': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'about_text': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
      }
           
class ReviewsForm(forms.ModelForm):
  """ Form, добавление и редактирование отзыва"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Reviews
    fields = [
        'avatar',
        'name',
        'slug',
        'date',
        'text',
        'status',
        'meta_h1',
        'meta_title',
        'meta_description',
        'meta_keywords',
    ]
    labels = {
        'avatar': 'Фотография пользователя',
        'name':'ФИО пользователя',
        'slug': 'URL',
        'date':'Дата коментария',
        'text':'Текст коментария',
        'status':'Статус публикации',
        'meta_h1':'Заголвок первого уровня',
        'meta_title':'Meta title',
        'untitle': 'Надзаголовок',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'date': forms.DateInput(attrs={
        'class':'form__controls',
      }),
      'text': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      })
    }
    
class StockForm(forms.ModelForm):
  """ Form, добавление и редактирование акций"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Stock
    fields = [
        'title',
        'slug',
        'description',
        'validity',
        'status',
        'image',
        'meta_title',
        'meta_description',
        'meta_keywords',
    ]
    labels = {
        'title':'Название акции',
        'slug': 'URL',
        'validity':'Срок действия акции',
        'description':'Текст коментария',
        'status':'Статус публикации',
        'image': 'Изображение акции',
        'meta_title':'Meta title',
        'untitle': 'Надзаголовок',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
      'title': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'validity': forms.DateInput(attrs={
        'class':'form__controls',
      }),
      'description': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form-controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      })
    }
       
class ServiceForm(forms.ModelForm):
  """ Form, добавление и редактирование услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Service
    fields = [
        'name',
        'slug',
        'subtitle',
        'status',
        'image',
        'meta_title',
        'meta_h1',
        'meta_description',
        'meta_keywords',
    ]
    labels = {
        'name':'Название',
        'slug': 'URL',
        'subtitle':'Текст под заголовком',
        'status':'Статус публикации',
        'image': 'Изображение акции',
        'meta_h1':'Meta h1',
        'meta_title':'Meta title',
        'untitle': 'Надзаголовок',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'subtitle': forms.DateInput(attrs={
        'class':'form__controls',
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      })
    }
    
class ServicePageForm(forms.ModelForm):
  """ Form, добавление и редактирование услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = ServicePage
    fields = [
        'name',
        'image',
        'meta_h1',
        'meta_title',
        'meta_description',
        'meta_keywords',
    ]
    labels = {
        'name':'Название',
        'image': 'Изображение',
        'meta_h1':'Meta h1',
        'meta_title':'Meta title',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form-controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      })
    }
    
class ServiceProductForm(forms.ModelForm):
  """ Form, добавление и редактирование услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = ServiceProduct
    fields = [
        'name',
        'slug',
        'status',
        'price',
        'service',
        'category',
        'image',
        'meta_title',
        'meta_h1',
        'meta_description',
        'meta_keywords',
    ]
    labels = {
        'name':'Название',
        'slug': 'URL',
        'status':'Статус публикации',
        'service':'Услуга',
        'price':'Цена',
        'category':'Категория',
        'image': 'Изображение акции',
        'meta_h1':'Meta h1',
        'meta_title':'Meta title',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'price': forms.TextInput(attrs={
        'class':'form__controls',
      }),
      'subtitle': forms.DateInput(attrs={
        'class':'form__controls',
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      }),
      'service': forms.Select(attrs={
        'class': 'form__controls'
      }),
      'category': forms.Select(attrs={
        'class': 'form__controls'
      })
    }
    
class ServiceCategoryForm(forms.ModelForm):
  """ Form, добавление и редактирование услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = ServiceCategory
    fields = [
        'name',
        'slug',
        'image',
        'meta_title',
        'meta_h1',
        'meta_description',
        'meta_keywords',
    ]
    labels = {
        'name':'Название',
        'slug': 'URL',
        'image': 'Изображение акции',
        'meta_h1':'Meta h1',
        'meta_title':'Meta title',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      })
    }
    
class ShopSettingsForm(forms.ModelForm):
    """ Form, отвечает за создание товара и редактирование товара"""
    # description = forms.CharField(label='Описание производителя', required=False, widget=CKEditorUploadingWidget)
    # description = forms.CharField(widget=TinyMCE())
    class Meta:
        model = ShopSettings
        fields = [
            'meta_h1',
            'meta_title',
            'meta_description',
            'meta_keywords',
        ]
        labels = {
            'meta_h1':'Заголвок первого уровня',
            'meta_title':'Meta title',
            'meta_description':'Мета description',
            'meta_keywords':'Meta keywords',
        }
        widgets = {
            'meta_h1': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_title': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_description': forms.Textarea(attrs={
                'class': 'form__controls',
                "id": "meta_description"
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
        }
        
class VacancySettingsForm(forms.ModelForm):
    """ Form, отвечает за создание товара и редактирование товара"""
    # description = forms.CharField(label='Описание производителя', required=False, widget=CKEditorUploadingWidget)
    # description = forms.CharField(widget=TinyMCE())
    class Meta:
        model = ShopSettings
        fields = [
            'meta_h1',
            'meta_title',
            'meta_description',
            'meta_keywords',
        ]
        labels = {
            'meta_h1':'Заголвок первого уровня',
            'meta_title':'Meta title',
            'meta_description':'Мета description',
            'meta_keywords':'Meta keywords',
        }
        widgets = {
            'meta_h1': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_title': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_description': forms.Textarea(attrs={
                'class': 'form__controls',
                "id": "meta_description"
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
        }
    


class GalleryForm(forms.ModelForm):
  """ Form, добавление и редактирование фотографий галлереи"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Gallery
    fields = [
        "image",
        "alt",
        "status"
    ]
    labels = {
        "image": "Изображение",
        "alt": "Альтернативный текст",
        "status": "Статус публикации ",
    }
    widgets = {
      'alt': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
    }