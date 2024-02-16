from django.http import HttpResponse
from django.shortcuts import render

from home.models import BaseSettings, HomeTemplate
from shop.models import Product
from reviews.models import Reviews




def index(request):
    page = request.GET.get('page', 1)
    
    home_page = HomeTemplate.objects.get()
    settings = BaseSettings.objects.get()
    product = Product.objects.all()
    reviews = Reviews.objects.filter(status=True)
    
    context = {
        "home_page": home_page,
        "products": product,
        "settings": settings,
        "reviews": reviews,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return HttpResponse('About page')

def contact(request):
    return render(request, "pages/contact.html")

def stock(request):
    return render(request, "pages/stock.html")
