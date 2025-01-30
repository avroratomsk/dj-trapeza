from django.db import models
from django.urls import reverse

from admin.singleton_model import SingletonModel

class BaseSettings(SingletonModel):
  logo  = models.ImageField(upload_to="base-settings", blank=True, null=True, verbose_name="Логотип")
  email = models.EmailField(max_length=250, blank=True, null=True, db_index=True, verbose_name="Email")
  meta_h1 = models.CharField(max_length=350, null=True, blank=True, verbose_name="Заголовок первого уровня")
  phone_whatsapp = models.CharField(max_length=350, null=True, blank=True, verbose_name="WhatsApp")
  vk = models.CharField(max_length=350, null=True, blank=True, verbose_name="VK")
  telegram = models.CharField(max_length=350, null=True, blank=True, verbose_name="Telegram")
  viber = models.CharField(max_length=350, null=True, blank=True, verbose_name="viber")
  instagram = models.CharField(max_length=350, null=True, blank=True, verbose_name="Instagram")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  

class HomeTemplate(SingletonModel):
  banner = models.ImageField(upload_to="home-page", blank=True, null=True, verbose_name="Картинка главной страницы")
  untitle = models.CharField(max_length=250, blank=True, null=True, verbose_name="Надзаголовок")
  left_text = models.TextField(null=True, blank=True, verbose_name="О нас левый текст")
  right_text = models.TextField(null=True, blank=True, verbose_name="О нас правый текст")
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  about_text = models.TextField(null=True, blank=True, verbose_name="О компании")
  about_image = models.ImageField(upload_to="home-page", null=True, blank=True, verbose_name="О компании картинка")
  callback_image = models.ImageField(upload_to="home-page", null=True, blank=True, verbose_name="CallBack картинка")
  callback_text = models.TextField(null=True, blank=True, verbose_name="CallBack текст")

class StockSettings(models.Model):
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  image = models.ImageField(upload_to="blog", blank=True, null=True, verbose_name="Изображение баннера")
  text = models.TextField(null=True, blank=True, verbose_name="Текст на странице")

class Stock(models.Model):
  """Model"""
  title = models.CharField(max_length=250, blank=True, null=True, verbose_name="Название акции")
  description = models.TextField(blank=True, null=True, verbose_name="Описание акции")
  validity = models.DateTimeField(blank=True, null=True, help_text="После окончания акции, она перейдет в состояние не активна", verbose_name="Срок дейстия акции")
  status = models.BooleanField(default=True, verbose_name="Статус публикации")
  image = models.ImageField(upload_to="stock", null=True, blank=True, verbose_name="Фотография акции")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")

  def get_absolute_url(self):
      return reverse("stock_detail", kwargs={"slug": self.slug})
    
class Gallery(models.Model):
  image = models.ImageField(upload_to="gallery", null=True, blank=True, verbose_name="Фотография товара")
  alt = models.CharField(max_length=250, blank=True, null=True, verbose_name="Альтернативный текст")
  status = models.BooleanField(default=True, verbose_name="Статус публикации ?")
  
class GallerySettings(SingletonModel):
  banner = models.ImageField(upload_to="about-page", blank=True, null=True, verbose_name="Баннер")
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  gallery_text = models.TextField(null=True, blank=True, verbose_name="Текс на странице")

class AboutTemplate(SingletonModel):
  banner = models.ImageField(upload_to="about-page", blank=True, null=True, verbose_name="Баннер")
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  about_text = models.TextField(null=True, blank=True, verbose_name="О компании")
  about_image = models.ImageField(upload_to="home-page", null=True, blank=True, verbose_name="О компании картинка")
  

class VacancySettings(SingletonModel):
  meta_h1 = models.CharField(max_length=350, null=True, blank=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="META заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="META описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="META keywords")
  

class Vacancy(models.Model):
  name = models.CharField(max_length=150, db_index=True, verbose_name="Наименование")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
  description = models.TextField(blank=True, null=True, verbose_name="Описание")
  price = models.CharField(max_length=150, db_index=True, blank=True, null=True, verbose_name="Зарплата")
  status = models.BooleanField(default=True, verbose_name="Статус публикации")
  meta_h1 = models.CharField(max_length=350, null=True, blank=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  
  # def get_absolute_url(self):
  #       return reverse("vacancy", kwargs={"slug": self.slug})

  
