from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
from home.models import AboutTemplate, BaseSettings, Gallery, HomeTemplate, Stock, StockSettings, Vacancy, GallerySettings
from blog.models import Post
from home.forms import CallbackForm, ContactForm, ReviewsForm, WriteToUsForm, ConsultForm
from .email_send import email_callback
from news.models import News
from service.models import Service
from shop.models import Category, Day, Product, Branch
from reviews.models import Reviews
from django.db.models import Q
import datetime
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', 1)
    try:
        home_page = HomeTemplate.objects.get()
        settings = BaseSettings.objects.get()
    except:
        home_page = HomeTemplate.objects.all()
        settings = BaseSettings.objects.all()
    
    stock = Stock.objects.filter(status=True)
    articles = Post.objects.filter(status=True) 
    news = News.objects.filter(status=True)
    reviews = Reviews.objects.filter(status=True)
    
    # Получаем из GET параметра page для пагинации
    page = request.GET.get("page", 1)
    category = Category.objects.all().exclude(slug="bez-kategorii")
    service = Service.objects.filter(status=True)
    
    # Получаем текущую дату
    current_date = datetime.datetime.now()

    # Получаем номер дня недели (0 для понедельника, 1 для вторника и т.д.)
    day_of_week = current_date.weekday()
    
    try:
        products = Product.objects.filter(day=day_of_week)
    except:
        pass

    paginator = Paginator(products, 8)
    current_page = paginator.page(int(page))
    current_slug = request.GET.get("slug")
    
    context = {
        "categorys": category,
        "current_slug": current_slug,
        "home_page": home_page,
        "products": current_page,
        "settings": settings,
        "reviews": reviews,
        "services": service,
        "stocks": stock,
        "articles": articles,
        "news": news,
    }
    return render(request, 'pages/index.html', context)


from django.urls import resolve

def get_breadcrumbs(request):
    breadcrumbs = []
    url_path = request.path
    url_names = url_path.strip("/").split("/")
    for index, url_name in enumerate(url_names):
        url = "/" + "/".join(url_names[:index+1])
        view_name = resolve(url).url_name
        breadcrumbs.append({'url': url, 'name': view_name})
    return breadcrumbs

def about(request):
    try:
        about_page = AboutTemplate.objects.get()
    except:
        about_page = AboutTemplate.objects.all()

    context = {
        "about_page": about_page,
        
    }
    
    return render(request, "pages/about.html", context)

def contact(request):
    return render(request, "pages/contact.html")

def stock(request):
    stocks = Stock.objects.filter(status=True)
    
    try:
      stock = StockSettings.objects.get()
    except:
      stock = StockSettings()
    
    context = {
        "stocks": stocks,
        "stock": stock
    }
    
    return render(request, "pages/stock/stock.html", context)

def stock_detail(request, slug):
    stock = Stock.objects.get(slug=slug)
    
    context = {
        "stock": stock
    }
    
    return render(request, "pages/stock/stock_detail.html", context)

def gallery(request):
    gallery = Gallery.objects.all()
    try:
        gallery_settings = GallerySettings.objects.get()
    except:
        gallery_settings = GallerySettings()

    context = {
        "gallery_settings": gallery_settings,
        "gallerys": gallery
    }
    
    return render(request, "pages/gallery.html", context)

def callback(request):
  if request.method == "POST":
    form = CallbackForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      privacy = form.cleaned_data['agreement']
      if privacy == True:
        privacy_text = "Да"
      else:
        privacy_text = "Нет"

      title = 'Заказ обратного звонка'
      messages = "Заказ обратного звонка:" + "\n" + "*ИМЯ*: " +str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone) + "\n" + "Пользователь согласился с обработкой персональных данных:: " + privacy_text

      email_callback(messages, title)
      return redirect(request.META.get('HTTP_REFERER'))
  else:
    form = CallbackForm()
  
  context = {
    'form': form
  }
  
  return render(request, 'pages/callback-succes.html', context)

def writetous(request):
  if request.method == "POST":
    form = WriteToUsForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      message = form.cleaned_data['message']
      privacy = form.cleaned_data['agreement']
      if privacy == True:
        privacy_text = "Да"
      else:
        privacy_text = "Нет"
      title = 'Форма Напишите нам'
      messages = "Заказ обратного звонка:" + "\n" + "*ИМЯ*: " +str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone) + "\n" + "*Сообщение*: " + str(message) + "\n" + "Пользователь согласился с обработкой персональных данных:: " + privacy_text
      
      email_callback(messages, title)
      return redirect(request.META.get('HTTP_REFERER'))
  else:
    form = WriteToUsForm()
  
  context = {
    'form': form
  }
  
  return render(request, 'pages/callback-succes.html', context)

def contacform(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      email = form.cleaned_data['email']
      message = form.cleaned_data['message']
      privacy = form.cleaned_data['agreement']
      if privacy == True:
        privacy_text = "Да"
      else:
        privacy_text = "Нет"
      title = 'Заявка со страницы контакты'
      messages = "Заказ обратного звонка:" + "\n" + "*ИМЯ*: " +str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone)  + "\n" + "*Email*: " + str(email) + "\n" + "*Сообщение*: " + str(message) + "\n" + "Пользователь согласился с обработкой персональных данных:: " + privacy_text
      
      email_callback(messages, title)
      return redirect(request.META.get('HTTP_REFERER'))
  else:
    form = ContactForm()
  
  context = {
    'form': form
  }
  
  return render(request, 'pages/callback-succes.html', context)

def consultation(request):
  if request.method == "POST":
    form = ConsultForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      data = form.cleaned_data['data']
      number = form.cleaned_data['number']
      reservation = form.cleaned_data['reservation']
      privacy = form.cleaned_data['agreement']
      if privacy == True:
        privacy_text = "Да"
      else:
        privacy_text = "Нет"
      title = 'Заказ консультации'
      messages = "Заказ консультации:" + "\n" + "ИМЯ: " +str(name) + "\n" + "ТЕЛЕФОН: " + str(phone)  + "\n" + "Дата бронирования: " + str(data) + "\n" + "Количество человек: " + str(number) + "\n" + "Зал: " + str(reservation) + "\n" + "Пользователь согласился с обработкой персональных данных:: " + privacy_text

      email_callback(messages, title)
      return redirect(request.META.get('HTTP_REFERER'))
  else:
    form = ConsultForm()

  context = {
    'form': form
  }

  return render(request, 'pages/callback-succes.html', context)

def reviewsform(request):
  if request.method == "POST":
    form = ReviewsForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      try:
        rating = form.cleaned_data['rating']
      except: 
          rating = 5  
      email = form.cleaned_data['email']
      message = form.cleaned_data['message']
      privacy = form.cleaned_data['agreement']
      if privacy == True:
        privacy_text = "Да"
      else:
        privacy_text = "Нет"
      title = 'Отзыв с сайта'
      messages = "Заказ обратного звонка:" + "\n" + "*ИМЯ*: " +str(name) + "\n" + "*Оценка*: " + str(rating)  + "\n" + "*Email*: " + str(email) + "\n" + "*Сообщение*: " + str(message) + "\n" + "Пользователь согласился с обработкой персональных данных:: " + privacy_text
      
      email_callback(messages, title)
      return redirect(request.META.get('HTTP_REFERER'))
  else:
    form = ReviewsForm()
  
  context = {
    'form': form
  }
  
  return render(request, 'pages/callback-succes.html', context)

def callback_success(request):
  return redirect(request.META.get('HTTP_REFERER'))

def vacancies(request):
  vacancy = Vacancy.objects.filter(status=True)
  
  context = {
    "vacancy": vacancy
  }
  return render(request, "pages/vacancies/vacancies.html", context)

def policy(request):
  return render(request, "pages/policy.html")

def cookie(request):
  return render(request, "pages/cookies.html")