from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from admin.singleton_model import SingletonModel

# Дни недели с краткими ключами и полнымим наименованиями.
DAY_NAMES = (
    ('mon', 'Понедельник'),
    ('tue', 'Вторник'),
    ('wed', 'Среда'),
    ('thu', 'Четверг'),
    ('fri', 'Пятница'),
    ('sat', 'Суббота'),
    ('sun', 'Воскресенье')
)

class ShopSettings(SingletonModel):
  meta_h1 = models.CharField(max_length=350, null=True, blank=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="META заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="META описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="META keywords")


class Category(models.Model):
  name = models.CharField(max_length=150, db_index=True, unique=True, verbose_name="Название категории")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
  image = models.ImageField(upload_to="category_image", blank=True, null=True, verbose_name="Изображение категории")
  meta_h1 = models.CharField(max_length=350, null=True, blank=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="META заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="META описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="META keywords")
  
  class Meta:
    db_table = 'category' 
    verbose_name = 'Категория'
    verbose_name_plural = "Категории"
    
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("category_detail", kwargs={"slug": self.slug})
  
  def get_category_url(self):
    return reverse("admin_product_category", kwargs={"id": self.id})


class Day(models.Model):
  name = models.CharField(max_length=50, db_index=True, blank=True, null=True, unique=True, verbose_name="Названия дня недел")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL day")
  num_day = models.PositiveIntegerField(default=0, verbose_name="Номер дня")
  
  class Meta:
    db_table = 'day'
    verbose_name = "День"
    verbose_name_plural = "Дня"
    ordering = ("id",)
  
  
  def __str__(self):
    return self.name
  
class Branch(models.Model):
  name = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Название филлиала")
  address_fillial = models.CharField(max_length=255, blank=True, null=True, verbose_name="Адрес филлиала")
  phone = models.CharField(max_length=50, blank=True, null=True, verbose_name="Номер телефона")
  time_work = models.CharField(max_length=250, null=True, blank=True, verbose_name="Режим работы")
  weekend = models.CharField(max_length=250, null=True, blank=True, verbose_name="Выходные дни")
  number_seats = models.CharField(max_length=50, null=True, blank=True, verbose_name="Количество посадочных мест")
  hall_rental = models.CharField(max_length=150, null=True, blank=True, verbose_name="Аренда зала")
  hall_rental_hollyday = models.CharField(max_length=150, null=True, blank=True, verbose_name="Аренда зала в праздники")
  scheme_payment = models.CharField(max_length=250, null=True, blank=True, verbose_name="Схема оплаты")
  map_code = models.TextField(null=True, blank=True, verbose_name="Код карты")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
  image = models.ImageField(upload_to="fillial", blank=True, null=True, verbose_name="Фотографии залов")
  
  def __str__(self):
    return f'{self.name}'

     
class Product(models.Model):
  name = models.CharField(max_length=150, db_index=True, verbose_name="Наименование продукта")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
  short_description = models.TextField(null=True, blank=True, verbose_name="Краткое описание")
  description = models.TextField(blank=True, null=True, verbose_name="Описание")
  meta_h1 = models.CharField(max_length=350, null=True, blank=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  image = models.ImageField(upload_to="product_iamge", blank=True, null=True, verbose_name="Изображение товара")
  price = models.CharField(max_length=150, db_index=True, blank=True, null=True, verbose_name="Цена товра")
  price_two = models.CharField(max_length=150, db_index=True, blank=True, null=True, verbose_name="Цена товра")
  discount = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name="Скидака в %")
  quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
  category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name='Категория')
  day = models.IntegerField(null=True, blank=True, verbose_name="Номер дня недели")
  branch = models.ManyToManyField(Branch, blank=True, verbose_name='Филлиал')
  weight = models.CharField(max_length=150, blank=True, null=True, verbose_name="Вес в граммах")
  weight_two = models.CharField(max_length=150, blank=True, null=True, verbose_name="Вес в граммах")
  calories = models.CharField(max_length=150, blank=True, null=True, verbose_name="Каллории")
  proteins = models.CharField(max_length=50, blank=True, null=True, verbose_name="Белки")
  fats = models.CharField(max_length=150, blank=True, null=True, verbose_name="Жиры")
  carbonhydrates = models.CharField(max_length=150, blank=True, null=True, verbose_name="Углеводы")
  status = models.BooleanField(default=True, verbose_name="Статус публикации")
  
  
  class Meta:
    db_table = 'product' 
    verbose_name = 'Продукт'
    verbose_name_plural = "Продукты"
    ordering = ("-id",)
    
  def get_all_children_products(self):
        children = self.children.all()
        products = []
        for child in children:
            products += child.products.filter(status=True)
        return products
  
    
  def __str__(self):
    return f'{self.name} Кол-во - {self.quantity}'
    
  """ Данный метод добавляет к id нули в начале """
  def display_id(self):
    return f'{self.id:05}' #self.id:05 - сделает так чтобы id состоял из 5 символов, если не хватате символов в начало добавить 0
  
  """ Данный метод возвращает цену со скидкой"""
  def sell_price(self):
    if self.discount:
      return round(self.price - self.price * self.discount / 100, 2)
    
    return self.price
  
  def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})


  
  
  
  
  