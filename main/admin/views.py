import os
import zipfile

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from admin.forms import CategoryForm, DayForm, FillialForm, GlobalSettingsForm, HomeTemplateForm, ProductForm, ReviewsForm, ServiceForm, StockForm, UploadFileForm
from home.models import BaseSettings, HomeTemplate, Stock
from main.settings import BASE_DIR
from service.models import Service
from reviews.models import Reviews
from shop.models import Product,Category,Day,Subsidiary
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
import openpyxl
import pandas as pd
# from django.contrib.auth.decorators import user_passes_test

# @user_passes_test(lambda u: u.is_superuser)
# def sidebar_show(request): 
   
#     request.session['sidebar'] = 'True' 
    
#     return redirect('admin')

# @user_passes_test(lambda u: u.is_superuser)

def admin(request):
  """Данная предстовление отобразает главную страницу админ панели"""
  product = Product.objects.all()
  context = {
    "product": product
  }
  return render(request, "page/index.html", context)

def admin_settings(request):
  try:
    settings = BaseSettings.objects.get()
  except:
    settings = BaseSettings()
    settings.save()
  
  if request.method == "POST":
    form_new = GlobalSettingsForm(request.POST, request.FILES, instance=settings)
    if form_new.is_valid():
      form_new.save()
      
      print("Все хорошо")
      # subprocess.call(["touch", RESET_FILE])
      return redirect("admin")
    else:
      return render(request, "settings/general_settings.html", {"form": form_new})

  settings = BaseSettings.objects.get()

  form = GlobalSettingsForm(instance=settings)
  context = {
    "form": form,
    "settings":settings
  }  

  return render(request, "settings/general_settings.html", context)

def admin_product(request):
  """
  View, которая возвращаяет и отрисовывает все товары на странице
  и разбивает их на пагинацию 
  """
  
  page = request.GET.get('page', 1)
  category = Category.objects.all()
  products = Product.objects.all()
  paginator = Paginator(products, 10)
  current_page = paginator.page(int(page))
  
  context = {
    "categorys": category,
    "products": current_page
  }
  return render(request, "shop/product/product.html", context)

def product_edit(request, pk):
  """
    View, которая получает данные из формы редактирования товара
    и изменяет данные внесенные данные товара в базе данных
  """
  product = Product.objects.get(id=pk)
  form = ProductForm(instance=product)
  
  form_new = ProductForm(request.POST, request.FILES, instance=product) 
  if request.method == 'POST':
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_product')
    else:
      return render(request, 'shop/product/product_edit.html', {'form': form_new,})
  context = {
    "form":form
  }
  return render(request, "shop/product/product_edit.html", context)

def product_add(request):
  form = ProductForm()
  
  if request.method == "POST":
    form_new = ProductForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_product')
    else:
      return render(request, "shop/product/product_add.html", {"form": form_new})
    
  context = {
    "form": form
  }
  
  return render(request, 'shop/product/product_add.html', context)

def product_delete(request,pk):
  product = Product.objects.get(id=pk)
  product.delete()
  
  return redirect('admin_product')


folder = 'upload/'

from PIL import Image

def upload_goods(request):
    form = UploadFileForm()
    if request.method == 'POST':
      form = UploadFileForm(request.POST, request.FILES)
      if form.is_valid():
          file = request.FILES['file']
          destination = open(os.path.join('upload/', file.name), 'wb+')
          for chunk in file.chunks():
              destination.write(chunk)
          destination.close()
              
          # Распаковка архива
          with zipfile.ZipFile('upload/upload.zip', 'r') as zip_ref:
              zip_ref.extractall('media/')
              
          # Удаление загруженного архива
          os.remove('upload/upload.zip')
          
          # Сжатие фотографий
          for filename in os.listdir('media/upload'):
            if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.JPG'):
              with Image.open(os.path.join('media/upload', filename)) as img:
                img.save(os.path.join('media/goods', filename), quality=60)  # quality=60 для JPEG файла
                
          # Очистка временной папки
          os.system('rm -rf media/upload')
          return redirect('upload-succes')
      else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})

def upload_succes(request):
  return render(request, "upload/upload-succes.html")


path = f"{BASE_DIR}/upload/upload.xlsx"

from pytils.translit import slugify
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

def parse_exсel(path):
  data = pd.read_excel(path)
  # Product.objects.all().delete()
  # Day.objects.all().delete()
  # Subsidiary.objects.all().delete()

  for index, row in data.iterrows():
    name = row['name']
    slug = slugify(row['name'])
    short_description = ''
    description = row['description']
    meta_h1 = ''
    meta_title = ''
    meta_description = ''
    meta_keywords = ''
    image = f"goods/{row['image']}"
    price = row['price']
    discount = 0.0
    quantity = 1.0
    category_name = row['category']
    category_slug = slugify(category_name)

    try:
      category = Category.objects.get(slug=category_slug)
    except ObjectDoesNotExist:
      if not Category.objects.filter(name=category_name).exists():
        category = Category.objects.create(
          name=category_name,
          slug=category_slug
        )
      else:
        category = Category.objects.filter(name=category_name).first()
    
    day_names = row['day'].split(';') if isinstance(row['day'], str) else []
    days = []
    
    for day_name in day_names:
      if day_name == "Понедельник" or day_name == "понедельник":
        day_slug = "Monday"
        num_day = 0
      if day_name == "Вторник" or day_name == "вторник":
        day_slug = "Tuesday"
        num_day = 1
      if day_name == "Среда" or day_name == "среда":
        day_slug = "Wednesday"
        num_day = 2
      if day_name == "Четверг" or day_name == "четверг":
        day_slug = "Thursday"
        num_day = 3
      if day_name == "Пятница" or day_name == "пятница":
        day_slug = "Friday"
        num_day = 4
      if day_name == "Суббота" or day_name == "суббота":
        day_slug = "Saturday"
        num_day = 5
      if day_name == "Воскресенье" or day_name == "Воскресенье":
        day_slug = "Sunday"
        num_day = 6
      if day_name == "Ежедневно" or day_name == "eжедневно":
        day_slug = "all_days"
        num_day = 7
      
      try:
        day = Day.objects.get(slug=day_slug)
      except Day.DoesNotExist: 
        day = Day.objects.create(name=day_name, slug=day_slug, num_day=num_day)
      days.append(day)
      
    branch_names = row['subsidiary'].split(';') if isinstance(row['subsidiary'], str) else []
    branchs = []
    
    for branch_name in branch_names:
      branch_name = branch_name.strip()
      branch_slug = slugify(branch_name)
      try:
        branch = Subsidiary.objects.get(slug=branch_slug)
      except Subsidiary.DoesNotExist:
        branch = Subsidiary.objects.create(name=branch_name, slug=branch_slug)
      branchs.append(branch)

    weight = ''
    calories = ''
    proteins = ''
    fats = ''
    carbonhydrates = ''
    status = True
  
    try:
      new_product = Product.objects.get(slug=slug)
    except ObjectDoesNotExist:
      if not Product.objects.filter(name=name).exists():
        new_product = Product.objects.create(
        name=name,
        slug=slug,
        short_description=short_description,
        description=description,
        meta_h1=meta_h1,
        meta_title=meta_title,
        meta_description=meta_description,
        meta_keywords=meta_keywords,
        image=image,
        price=price,
        discount=discount,
        quantity=quantity,
        category=category,
        weight=weight,
        calories=calories,
        proteins=proteins,
        fats=fats,
        carbonhydrates=carbonhydrates,
        status=status
      )
      else:
        new_product = Product.objects.filter(name=name).first()  

    try:
      pr = Product.objects.filter(name=new_product.name)
      for day_add in days:
          pr[0].day.add(day_add) 
      
      for branch_add in branchs:
        pr[0].subsidiary.add(branch_add)
        
      new_product.save()
    except IntegrityError:
      # Обработка ошибки при сохранении объекта, если возник конфликт по ключу
      pass
  
# parse_exсel(path)

def admin_category(request):
  categorys = Category.objects.all()
  
  context ={
    "categorys": categorys,
  }
  return render(request, "shop/category/category.html", context)

def category_add(request):
  form = CategoryForm()
  if request.method == "POST":
    form_new = CategoryForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_category")
    else:
      return render(request, "shop/category/category_add.html", {"form": form_new})
    
  context = {
    "form": form
  }
  return render(request, "shop/category/category_add.html", context)

def category_edit(request, pk):
  categorys = Category.objects.get(id=pk)
  if request.method == "POST":
    form = CategoryForm(request.POST, request.FILES, instance=categorys)
    if form.is_valid():
      form.save()
      return redirect("admin_category")
    else:
      return render(request, "shop/category/category_edit.html", {"form": form})
  
  context = {
    "form": CategoryForm(instance=categorys),
    "categorys": categorys
  }

  return render(request, "shop/category/category_edit.html", context)

def category_delete(request, pk):
  category = Category.objects.get(id=pk)
  category.delete()
  
  return redirect('admin_category')

def day_product(request):
  days = Day.objects.all().exclude(slug="ezhednevno")
  
  context = {
    "days": days,
  }
  
  return render(request, "days/days.html", context)

def day_edit(request, pk):
  day = Day.objects.get(id=pk)
  form = DayForm(instance=day)
  
  form_new = DayForm(request.POST, instance=day)
  if request.method == "POST":
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_day")
    else:
      return render(request, "days/days_edit.html", {"form": form_new})

  context = {
    "form": form,
  }
  
  return render(request, "days/days_edit.html", context)

def day_add(request):
  form = DayForm()
  if request.method == "POST":
    form_new = DayForm(request.POST)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_day")
    else:
      return render(request, "days/days_add.html", {"form": form_new})
  context = {
    "form": form
  }
  
  return render(request, "days/days_add.html", context)

def admin_fillial(request):
  fillials = Subsidiary.objects.all()
  
  context = {
    "fillials": fillials
  }
  
  return render(request, "fillials/fillial.html", context)

def fillial_edit(request, pk):
  fillial = Subsidiary.objects.get(id=pk)
  form = FillialForm(instance=fillial)
  
  if request.method == "POST":
    form_new = FillialForm(request.POST, request.FILES, instance=fillial)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_fillial")
    else:
      return render(request, "fillials/fillial_edit.html", {"form": form_new})
  
  context = {
    "form": form,
  }
  
  return render(request, "fillials/fillial_edit.html", context)

def fillial_add(request):
  form = FillialForm()
  if request.method == "POST":
    form_new = FillialForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_fillial")
    else:
      return render(request, "fillials/fillial_add.html", {"form": form_new})
    
  context = {
    "form": form
  }
  
  return render(request, "fillials/fillial_add.html", context)

def admin_home(request):
  try:
    home_page = HomeTemplate.objects.get()
  except:
    home_page = HomeTemplate()
    home_page.save()
    
  if request.method == "POST":
    form_new = HomeTemplateForm(request.POST, request.FILES, instance=home_page)
    if form_new.is_valid():
      form_new.save()
      
      print("Все хорошо")
      # subprocess.call(["touch", RESET_FILE])
      return redirect("admin")
    else:
      return render(request, "static/home_page.html", {"form": form_new})
  
  home_page = HomeTemplate.objects.get()
  
  form = HomeTemplateForm(instance=home_page)
  context = {
    "form": form,
    "home_page":home_page
  }  
  
  return render(request, "static/home_page.html", context)

def admin_reviews(request):
  reviews = Reviews.objects.all()
  
  context = {
    "reviews": reviews
  }
  
  return render(request, "reviews/reviews.html", context)

def admin_reviews_edit(request, pk):
  review = Reviews.objects.get(id=pk)
  form = ReviewsForm(instance=review)
  
  if request.method == "POST":
    form_new = ReviewsForm(request.POST, request.FILES, instance=review)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_reviews")
    else:
      return render(request, "reviews/reviews_edit.html", {"form": form_new})
  
  context = {
    "review":review,
    "form": form
  }
  
  return render(request, "reviews/reviews_edit.html", context)

def admin_reviews_add(request):
  form = ReviewsForm()
  if request.method == "POST":
    form_new = ReviewsForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_reviews")
    else:
      return render(request, "reviews/reviews_add.html", {"form": form_new})
    
  context = {
    "form": form
  }
  
  return render(request, "reviews/reviews_add.html", context)

def admin_stock(request):
  stocks = Stock.objects.all()
  
  context = {
    "stocks": stocks
  }
  
  return render(request, "stock/stock.html", context)

def stock_add(request):
  form = StockForm()
  
  if request.method == "POST":
    form_new = StockForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_stock")
    else: 
      return render(request, "stock/stock_add.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "stock/stock_add.html", context)

def stock_edit(request, pk):
  stock = Stock.objects.get(id=pk)
  form = StockForm(instance=stock)
  if request.method == "POST":
    form_new = StockForm(request.POST, request.FILES, instance=stock)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_stock")
    else:
      return render(request, "stock/stock_edit.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "stock/stock_edit.html", context)

def stock_delete(request, pk):
  stock = Stock.objects.get(id=pk)
  stock.delete()
  return redirect("admin_stock")

def admin_service(request):
  services = Service.objects.all()
  
  context = {
    "services": services
  }
  
  return render(request, "serv/admin_serv.html", context)

def service_add(request):
  form = ServiceForm()
  
  if request.method == "POST":
    form_new = ServiceForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_service")
    else: 
      return render(request, "serv/serv_add.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "serv/serv_add.html", context)

def service_edit(request, pk):
  services = Service.objects.get(id=pk)
  form = ServiceForm(instance=services)
  if request.method == "POST":
    form_new = ServiceForm(request.POST, request.FILES, instance=services)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_service")
    else:
      return render(request, "serv/stock_edit.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "serv/serv_edit.html", context)

def service_delete(request, pk):
  service = Service.objects.get(id=pk)
  service.delete()
  return redirect("admin_service")

def admin_colors(request):
  context = {
    "title": "Настройки цветовой схемы сайта"
  }
  return render(request, "settings/color_scheme.html", context)