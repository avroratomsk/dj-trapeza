from django.http import HttpResponse
from django.shortcuts import render

from home.models import BaseSettings, HomeTemplate
from shop.models import Product




def index(request):
    page = request.GET.get('page', 1)
    
    home_page = HomeTemplate.objects.get()
    settings = BaseSettings.objects.get()
    product = Product.objects.all()
    
    context = {
        "home_page": home_page,
        "products": product,
        "settings": settings,
        'title': "Столовая трапеза",
        'content': "Контент главной страницы"
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return HttpResponse('About page')
