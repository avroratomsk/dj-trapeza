from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import AboutTemplate, BaseSettings, Gallery, HomeTemplate, Stock
from blog.models import Post
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
    
    context = {
        "stocks": stocks
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
    
    context = {
        "gallerys": gallery
    }
    
    return render(request, "pages/gallery.html", context)

def callback(request):
  ...
