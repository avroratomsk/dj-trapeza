from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import BaseSettings, HomeTemplate, Stock
from shop.models import Day, Product, Subsidiary
from reviews.models import Reviews
from django.db.models import Q
from django.core.paginator import Paginator




def index(request):
    page = request.GET.get('page', 1)
    try:
        home_page = HomeTemplate.objects.get()
        settings = BaseSettings.objects.get()
    except:
        home_page = HomeTemplate.objects.all()
        settings = BaseSettings.objects.all()
        
    reviews = Reviews.objects.filter(status=True)
     # Получаем из GET параметра page для пагинации
    page = request.GET.get("page", 1)
    
    # Получаем текущий день из таблицы Day
    current_day = Day.objects.get(num_day=datetime.today().weekday())
    
    # Получаем выбранный день из GET параметра day
    selected_day = request.GET.get("day", None)
    
    # Делаем проверку и в зависимости от действий пользователя выводить продукцию
    if selected_day:
        products = Product.objects.filter(Q(day__slug=selected_day) | Q(day__slug="all_days"))
    else:
        products = Product.objects.filter(Q(day__id=current_day.id) | Q(day__slug="all_days"))

    paginator = Paginator(products, 8)
    current_page = paginator.page(int(page))
    current_slug = request.GET.get("slug")
    current_slug = request.GET.get("slug")
    
    context = {
        "current_slug": current_slug,
        "home_page": home_page,
        "products": current_page,
        "settings": settings,
        "reviews": reviews,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, "pages/about.html")

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
