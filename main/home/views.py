from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
from home.models import AboutTemplate, BaseSettings, Gallery, HomeTemplate, Stock
from blog.models import Post
from home.forms import CallbackForm
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
    if request.method == 'POST':

        form = CallbackForm(request.POST)
        name = request.POST['name']
        tel = request.POST['phone']

        message = f"Заказ обратного звонка:nИМЯ: {name}nТЕЛЕФОН: {tel}"

        if form.is_valid():
            title = 'Заказ обратного звонка'
            email_callback(title, message)
            return redirect("home")

        else:
            return HttpResponse("Форма имеет ошибки. Пожалуйста, проверьте введенные данные.")
    
    return HttpResponse("Метод не POST. Пожалуйста, отправьте форму используя метод POST.")

def vacancies(request):
    return render(request, "pages/vacancies/vacancies.html")