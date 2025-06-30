import os
import zipfile

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from admin.forms import GalleryTemplateForm, AboutTemplateForm, BanketForm, BlogPage, CategoryForm, DayForm, FillialForm, GalleryForm, GlobalSettingsForm, HomeTemplateForm, NewsForm, NewsPage, PominalnyeForm, PostForm, ProductForm, ReviewsForm, ServiceCategoryForm, ServiceForm, ServicePageForm, ServiceProductForm, ShopSettingsForm, StockForm, StockPage, UploadFileForm, VacancyForm, VacancySettingsForm
from home.models import AboutTemplate, BaseSettings, Gallery, HomeTemplate, Stock, StockSettings, Vacancy, VacancySettings, GallerySettings
from blog.models import BlogSettings, Post
from news.models import News, NewsSettings
from main.settings import BASE_DIR
from service.models import Banket, PominalnyeObed, Service, ServiceCategory, ServicePage, ServiceProduct
from reviews.models import Reviews
from shop.models import Product,Category,Day,Branch, ShopSettings
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
import openpyxl
import pandas as pd
from django.contrib.auth.decorators import user_passes_test

# @user_passes_test(lambda u: u.is_superuser)
# def sidebar_show(request): 
   
#     request.session['sidebar'] = 'True' 
    
#     return redirect('admin')

# @user_passes_test(lambda u: u.is_superuser)

@user_passes_test(lambda u: u.is_superuser)
def admin(request):
  """Данная предстовление отобразает главную страницу админ панели"""
  product = Product.objects.all()
  context = {
    "product": product
  }
  return render(request, "page/index.html", context)

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def admin_product(request):
  """
  View, которая возвращаяет и отрисовывает все товары на странице
  и разбивает их на пагинацию 
  """
  page = request.GET.get('page', 1)
  category = Category.objects.all().order_by('id')
  # products = Product.objects.all().exclude(funeral_menu=True)
  products = Product.objects.all().order_by('id')
  paginator = Paginator(products, 10)
  current_page = paginator.page(int(page))
  context = {
    "categorys": category,
    "products": current_page
  }
  return render(request, "shop/product/product.html", context)

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def product_delete(request,pk):
  product = Product.objects.get(id=pk)
  product.delete()
  
  return redirect('admin_product')

@user_passes_test(lambda u: u.is_superuser)
def admin_blog(request):
  """
  View, которая возвращаяет и отрисовывает все товары на странице
  и разбивает их на пагинацию 
  """
  posts = Post.objects.all().order_by('id')
  context = {
    "posts": posts
  }
  return render(request, "blog/blog_post/blog_post.html", context)

@user_passes_test(lambda u: u.is_superuser)
def blog_add(request):
  form = PostForm()
  
  if request.method == "POST":
    form_new = PostForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_blog')
    else:
      return render(request, "blog/blog_post/post_add.html", {"form": form_new})
    
  context = {
    "form": form
  }
  
  return render(request, "blog/blog_post/post_add.html", context)

@user_passes_test(lambda u: u.is_superuser)
def blog_edit(request, pk):
  """
    View, которая получает данные из формы редактирования товара
    и изменяет данные внесенные данные товара в базе данных
  """
  post = Post.objects.get(id=pk)
  form = PostForm(instance=post)
  
  form_new = PostForm(request.POST, request.FILES, instance=post) 
  if request.method == 'POST':
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_blog')
    else:
      return render(request, "blog/blog_post/post_edit.html", {"form": form_new})
  context = {
    "form":form
  }
  return render(request, "blog/blog_post/post_edit.html", context)

@user_passes_test(lambda u: u.is_superuser)
def blog_delete(request, pk):
  post = Post.objects.get(id=pk)
  post.delete()
  
  return redirect('admin_blog')

@user_passes_test(lambda u: u.is_superuser)
def admin_news(request):
  """
  View, которая возвращаяет и отрисовывает все товары на странице
  и разбивает их на пагинацию 
  """
  news = News.objects.all().order_by('id')
  context = {
    "news": news
  }
  return render(request, "news/new/news.html", context)

@user_passes_test(lambda u: u.is_superuser)
def news_add(request):
  form = NewsForm()
  
  if request.method == "POST":
    form_new = NewsForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_news')
    else:
      return render(request, "news/new/new_add.html", {"form": form_new})
    
  context = {
    "form": form
  }
  
  return render(request, "news/new/new_add.html", context)

@user_passes_test(lambda u: u.is_superuser)
def news_edit(request, pk):
  """
    View, которая получает данные из формы редактирования товара
    и изменяет данные внесенные данные товара в базе данных
  """
  news = News.objects.get(id=pk)
  form = NewsForm(instance=news)
  
  form_new = NewsForm(request.POST, request.FILES, instance=news) 
  if request.method == 'POST':
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_news')
    else:
      return render(request, "news/new/new_edit.html", {"form": form_new})
  context = {
    "form":form
  }
  return render(request, "news/new/new_add.html", context)

@user_passes_test(lambda u: u.is_superuser)
def news_delete(request, pk):
  news = News.objects.get(id=pk)
  news.delete()
  
  return redirect('admin_news')

@user_passes_test(lambda u: u.is_superuser)
def product_day_edit(request, id):
  product = Product.objects.get(id=id)
  if request.method == "POST":
    set_day = request.POST['set-day']
    product.day = set_day
    product.save()
    return redirect(request.META.get('HTTP_REFERER'))

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt  # Убери если используешь CSRF через токен в JS
def reset_day_by_category(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        category_id = data.get("category_id")

        if not category_id:
            return JsonResponse({"success": False, "error": "No category ID"}, status=400)

        updated = Product.objects.filter(category_id=category_id).update(day=None)  # или day=0

        return JsonResponse({"success": True, "updated": updated})

    return JsonResponse({"success": False, "error": "Invalid request"}, status=405)
folder = 'upload/'

from PIL import Image

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def upload_succes(request):
  return render(request, "upload/upload-succes.html")


path = f"{BASE_DIR}/upload/upload.xlsx"

from pytils.translit import slugify
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

@user_passes_test(lambda u: u.is_superuser)
def parse_exсel(path):
  workbook = openpyxl.load_workbook(path)
  sheet = workbook.active
  start_row = 2
  Product.objects.all().delete()
  # Day.objects.all().delete()
  # Branch.objects.all().delete()

  for row in sheet.iter_rows(min_row=start_row, values_only=True):
    name = row[1]
    slug = slugify(name)
    short_description = ''
    description = row[3]
    meta_h1 = ''
    meta_title = ''
    meta_description = ''
    meta_keywords = ''
    image = f"goods/{row[4]}"
    price = row[5]
    price_two = row[6]
    discount = 0.0
    quantity = 1.0
    category_name = row[8]
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
    
      
    branch_names = row[13].split(';') if isinstance(row[13], str) else []
    branchs = []
    
    for branch_name in branch_names:
      branch_name = branch_name.strip()
      branch_slug = slugify(branch_name)
      try:
        branch = Branch.objects.get(slug=branch_slug)
      except Branch.DoesNotExist:
        branch = Branch.objects.create(name=branch_name, slug=branch_slug)
      branchs.append(branch)

    weight = row[11]
    weight_two = row[12]
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
        price_two=price_two,
        discount=discount,
        quantity=quantity,
        category=category,
        weight=weight,
        weight_two=weight_two,
        calories=calories,
        proteins=proteins,
        fats=fats,
        carbonhydrates=carbonhydrates,
        status=status
      )
      else:
        new_product = Product.objects.filter(name=name).first()  

  
# parse_exсel(path)

@user_passes_test(lambda u: u.is_superuser)
def admin_category(request):
  categorys = Category.objects.all().order_by('id')
  
  context ={
    "categorys": categorys,
  }
  return render(request, "shop/category/category.html", context)

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
  category = Category.objects.get(id=pk)
  category.delete()
  
  return redirect('admin_category')

@user_passes_test(lambda u: u.is_superuser)
def admin_product_category(request, id):
  category = Category.objects.all().order_by('id')
  product = Product.objects.filter(category_id=id)

  reset_btn = True

  context = {
    "categorys": category,
    "products": product,
    "reset_btn": reset_btn
  }
  
  return render(request, "shop/product/product.html", context)

@user_passes_test(lambda u: u.is_superuser)
def day_product(request):
  days = Day.objects.all().exclude(slug="ezhednevno")
  
  context = {
    "days": days,
  }
  
  return render(request, "days/days.html", context)

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def admin_fillial(request):
  fillials = Branch.objects.all().order_by('id')
  
  context = {
    "fillials": fillials
  }
  
  return render(request, "fillials/fillial.html", context)

@user_passes_test(lambda u: u.is_superuser)
def fillial_edit(request, pk):
  fillial = Branch.objects.get(id=pk)
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

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "static/home_page.html", {"form": form_new})
  
  home_page = HomeTemplate.objects.get()
  
  form = HomeTemplateForm(instance=home_page)
  
  context = {
    "form": form,
    "home_page":home_page
  }  
  
  return render(request, "static/home_page.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_gallery_settings(request):
  try:
    gallery_page = GallerySettings.objects.get()
  except:
    gallery_page = GallerySettings()
    gallery_page.save()

  if request.method == "POST":
    form_new = GalleryTemplateForm(request.POST, request.FILES, instance=gallery_page)
    if form_new.is_valid():
      form_new.save()
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "static/home_page.html", {"form": form_new})

  #gallery_page = GallerySettings.objects.get()

  form = GalleryTemplateForm(instance=gallery_page)

  context = {
    "form": form,
    "gallery_page":gallery_page
  }

  return render(request, "static/gallery_page.html", context)

@user_passes_test(lambda u: u.is_superuser)
def pomin_page(request):
  try:
    pomin_page = PominalnyeObed.objects.get()
  except:
    pomin_page = PominalnyeObed()
    pomin_page.save()
    
  if request.method == "POST":
    form_new = PominalnyeForm(request.POST, request.FILES, instance=pomin_page)
    if form_new.is_valid():
      form_new.save()
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "static/pomin.html", {"form": form_new})
  
  pomin_page = PominalnyeObed.objects.get()
  
  form = PominalnyeForm(instance=pomin_page)
  
  context = {
    "form": form,
    "pomin_page":pomin_page
  }  
  
  return render(request, "static/pomin.html", context)

@user_passes_test(lambda u: u.is_superuser)
def banket_page(request):
  try:
    banket_page = Banket.objects.get()
  except:
    banket_page = Banket()
    banket_page.save()
    
  if request.method == "POST":
    form_new = BanketForm(request.POST, request.FILES, instance=banket_page)
    if form_new.is_valid():
      form_new.save()
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "static/banket.html", {"form": form_new})
  
  banket_page = Banket.objects.get()
  
  form = BanketForm(instance=banket_page)
  
  context = {
    "form": form,
    "banket_page":banket_page
  }  
  
  return render(request, "static/banket.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_about(request):
  try:
    about_page = AboutTemplate.objects.get()
  except:
    about_page = AboutTemplate()
    about_page.save()
    
  if request.method == "POST":
    form_new = AboutTemplateForm(request.POST, request.FILES, instance=about_page)
    if form_new.is_valid():
      form_new.save()
      
      return redirect("admin")
    else:
      return render(request, "static/about_page.html", {"form": form_new})
  
  about_page = AboutTemplate.objects.get()
  
  form = AboutTemplateForm(instance=about_page)
  context = {
    "form": form,
    "about_page":about_page
  }  
  
  return render(request, "static/about_page.html", context)

@user_passes_test(lambda u: u.is_superuser)
def news_settings(request):
  try:
    news_set = NewsSettings.objects.get()
  except:
    news_set = NewsSettings()
    news_set.save()
    
  if request.method == "POST":
    form_new = NewsPage(request.POST, request.FILES, instance=news_set)
    if form_new.is_valid():
      form_new.save()
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "news/news_settings.html", {"form": form_new})
  
  news_set = NewsSettings.objects.get()
  
  form = NewsPage(instance=news_set)
  
  context = {
    "form": form,
    "news_set": news_set
  }  
  
  return render(request, "news/news_settings.html", context)

@user_passes_test(lambda u: u.is_superuser)
def stock_settings(request):
  try:
    stock_set = StockSettings.objects.get()
  except:
    stock_set = StockSettings()
    stock_set.save()
    
  if request.method == "POST":
    form_new = StockPage(request.POST, request.FILES, instance=stock_set)
    if form_new.is_valid():
      form_new.save()
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "stock/stock_settings.html", {"form": form_new})
  
  stock_set = StockSettings.objects.get()
  
  form = StockPage(instance=stock_set)
  
  context = {
    "form": form,
    "stock_set": stock_set
  }  
  
  return render(request, "stock/stock_settings.html", context)

@user_passes_test(lambda u: u.is_superuser)
def blog_settings(request):
  try:
    blog_set = BlogSettings.objects.get()
  except:
    blog_set = BlogSettings()
    blog_set.save()
    
  if request.method == "POST":
    form_new = BlogPage(request.POST, request.FILES, instance=blog_set)
    if form_new.is_valid():
      form_new.save()
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "blog/blog_settings.html", {"form": form_new})
  
  blog_set = BlogSettings.objects.get()
  
  form = BlogPage(instance=blog_set)
  
  context = {
    "form": form,
    "blog_set":blog_set
  }  
  
  return render(request, "blog/blog_settings.html", context)

@user_passes_test(lambda u: u.is_superuser)
def blog_page(request):
  try:
    blog_page = BlogSettings.objects.get()
  except:
    blog_page = BlogSettings()
    blog_page.save()
    
  if request.method == "POST":
    form_new = BlogPage(request.POST, request.FILES, instance=blog_page)
    if form_new.is_valid():
      form_new.save()
      
      return redirect("admin")
    else:
      return render(request, "static/blog_page.html", {"form": form_new})
  
  blog_page = BlogSettings.objects.get()
  
  form = BlogPage(instance=blog_page)
  context = {
    "form": form,
    "about_page":blog_page
  }  
  
  return render(request, "static/blog_page.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_reviews(request):
  reviews = Reviews.objects.all().order_by('id')
  
  context = {
    "reviews": reviews
  }
  
  return render(request, "reviews/reviews.html", context)

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def admin_stock(request):
  stocks = Stock.objects.all().order_by('id')
  
  context = {
    "stocks": stocks
  }
  
  return render(request, "stock/stock.html", context)

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def stock_delete(request, pk):
  stock = Stock.objects.get(id=pk)
  stock.delete()
  return redirect("admin_stock")

@user_passes_test(lambda u: u.is_superuser)
def service_page(request):
  try:
    service_page = ServicePage.objects.get()
  except:
    service_page = ServicePage()
    service_page.save()
    
  if request.method == "POST":
    form_new = ServicePageForm(request.POST, request.FILES, instance=service_page)
    if form_new.is_valid():
      form_new.save()
      # subprocess.call(["touch", RESET_FILE]) # restart app django
      return redirect("admin")
    else:
      return render(request, "serv/serv_page.html", {"form": form_new})
  
  service_page = ServicePage.objects.get()
  
  form = ServicePageForm(instance=service_page)
  context = {
    "form": form,
    "service_page":service_page
  }  

  return render(request, "serv/serv_page.html", context)


@user_passes_test(lambda u: u.is_superuser)
def admin_service(request):
  services = Service.objects.all().order_by('id')
  
  context = {
    "products": services
  }
  
  return render(request, "serv/admin_serv.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_shop(request):
  """Настройки магазина"""
  try:
    shop_setup = ShopSettings.objects.get()
    form = ShopSettingsForm(instance=shop_setup)
  except:
    form = ShopSettingsForm()
    
  if request.method == "POST":
    shop_setup = ShopSettings.objects.get()
    form_new = ShopSettingsForm(request.POST, request.FILES, instance=shop_setup)
    
    if form_new.is_valid:
      form_new.save()
      
      return redirect('admin_shop')
    else:
      return render(request, "shop/settings.html", {"form": form})
  
  context = {
    "form": form,
  }  
  return render(request, "shop/settings.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_vacancy(request):
  """Настройки Вакансий"""
  try:
    vacancy_setup = VacancySettings.objects.get()
    form = VacancySettingsForm(instance=vacancy_setup)
  except:
    form = VacancySettingsForm()
    
  if request.method == "POST":
    vacancy_setup = VacancySettings.objects.get()
    form_new = VacancySettingsForm(request.POST, request.FILES, instance=vacancy_setup)
    
    if form_new.is_valid:
      form_new.save()
      
      return redirect('admin_shop')
    else:
      return render(request, "vacancy/vacancy_settings.html", {"form": form})
  
  context = {
    "form": form,
  }  
  return render(request, "vacancy/vacancy_settings.html", context)

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def service_delete(request, pk):
  service = Service.objects.get(id=pk)
  service.delete()
  return redirect("admin_service")


@user_passes_test(lambda u: u.is_superuser)
def service_product(request):
  product = ServiceProduct.objects.filter(status=True).order_by('-id')
  
  context = {
    "products": product
  }
  
  return render(request, "serv/serv_product.html", context)

@user_passes_test(lambda u: u.is_superuser)
def service_product_add(request):
  form = ServiceProductForm()
  
  if request.method == "POST":
    form_new = ServiceProductForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("service_product")
    else: 
      return render(request, "serv/serv_product_add.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "serv/serv_product_add.html", context)

@user_passes_test(lambda u: u.is_superuser)
def service_product_edit(request, pk):
  product = ServiceProduct.objects.get(id=pk)
  form = ServiceProductForm(instance=product)
  if request.method == "POST":
    form_new = ServiceProductForm(request.POST, request.FILES, instance=product)
    if form_new.is_valid():
      form_new.save()
      return redirect("service_product")
    else:
      return render(request, "serv/serv_product_edit.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "serv/serv_product_edit.html", context)

@user_passes_test(lambda u: u.is_superuser)
def service_product_delete(request, pk):
  product = ServiceProduct.objects.get(id=pk)
  product.delete()
  return redirect(service_product)

@user_passes_test(lambda u: u.is_superuser)
def service_category(request):
  category = ServiceCategory.objects.all().order_by('id')
  
  context = {
    "categorys": category
  }
  
  return render(request, "serv/serv_category.html", context)

@user_passes_test(lambda u: u.is_superuser)
def service_category_add(request):
  form = ServiceCategoryForm()
  
  if request.method == "POST":
    form_new = ServiceCategoryForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("service_category")
    else: 
      return render(request, "serv/serv_category_add.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "serv/serv_category_add.html", context)

@user_passes_test(lambda u: u.is_superuser)
def service_category_edit(request, pk):
  category = ServiceCategory.objects.get(id=pk)
  form = ServiceCategoryForm(instance=category)
  if request.method == "POST":
    form_new = ServiceCategoryForm(request.POST, request.FILES, instance=category)
    if form_new.is_valid():
      form_new.save()
      return redirect("service_category")
    else:
      return render(request, "serv/serv_category_edit.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "serv/serv_category_edit.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_colors(request):
  context = {
    "title": "Настройки цветовой схемы сайта"
  }
  return render(request, "settings/color_scheme.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_gallery(requets):
  gallery = Gallery.objects.all().order_by('id')
  context = {
    "gallerys": gallery
  }
  return render(requets, "gallery/gallery.html", context)

@user_passes_test(lambda u: u.is_superuser)
def gallery_add(request):
  form = GalleryForm()
  
  if request.method == "POST":
    form_new = GalleryForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_gallery")
    else: 
      return render(request, "gallery/gallery_add.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "gallery/gallery_add.html", context)

@user_passes_test(lambda u: u.is_superuser)
def gallery_edit(request, pk):
  gallery = Gallery.objects.get(id=pk)
  form = GalleryForm(instance=gallery)
  if request.method == "POST":
    form_new = GalleryForm(request.POST, request.FILES, instance=gallery)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_gallery")
    else:
      return render(request, "gallery/gallery_edit.html", {"form": form_new})
  
  context = {
    "form": form
  }
  
  return render(request, "gallery/gallery_edit.html", context)

@user_passes_test(lambda u: u.is_superuser)
def gallery_delete(request, pk):
  gallery = Gallery.objects.get(id=pk)
  gallery.delete()
  return redirect("admin_gallery")

@user_passes_test(lambda u: u.is_superuser)
def vacancys(request):
  vacancys = Vacancy.objects.all().order_by('id')
  context = {
    "products": vacancys,
  }
  return render(request, "vacancy/vacancy.html", context)

@user_passes_test(lambda u: u.is_superuser)
def vacancy_edit(request, pk):
  """
    View, которая получает данные из формы редактирования товара
    и изменяет данные внесенные данные товара в базе данных
  """
  vacancy = Vacancy.objects.get(id=pk)
  form = VacancyForm(instance=vacancy)
  
  form_new = VacancyForm(request.POST, request.FILES, instance=vacancy) 
  if request.method == 'POST':
    if form_new.is_valid():
      form_new.save()
      return redirect('vacancys')
    else:
      return render(request, 'vacancy/vacancy_edit.html', {'form': form_new})
  context = {
    "form":form
  }
  return render(request, "vacancy/vacancy_edit.html", context)

@user_passes_test(lambda u: u.is_superuser)
def vacancy_add(request):
  form = VacancyForm()
  
  if request.method == "POST":
    form_new = VacancyForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect('vacancys')
    else:
      return render(request, "vacancy/vacancy_add.html", {"form": form_new})
    
  context = {
    "form": form
  }
  
  return render(request, 'vacancy/vacancy_add.html', context)

@user_passes_test(lambda u: u.is_superuser)
def vacancy_delete(request,pk):
  vacancy = Vacancy.objects.get(id=pk)
  vacancy.delete()
  
  return redirect('vacancys')