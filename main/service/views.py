from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from shop.models import Category, Product
from service.models import Service, ServicePage

def service(request):
  services = Service.objects.filter(status=True)
  try:
    # Пытаемся получить объект ServicePage
    service_page = ServicePage.objects.get()
    # Если объект найден, можете продолжать выполнение кода
  except ObjectDoesNotExist:
    # Обработка случая, когда объект не найден
    print("ServicePage не найден")
    # Дополнительные действия на ваше усмотрение
  
  context = {
    "service_page": service_page,
    "services": services
  }
  return render(request, "pages/service/service.html", context)

def service_detail(request, slug):
  category = Category.objects.all()
  service = Service.objects.get(slug=slug)
  if(slug == "organizatsiya-banketov"):
    try:
      product = Product.objects.filter(banquet_menu_checkbox=True)
    except:
      pass
  
  if(slug == "pominalnye-obedy"):
    product = Product.objects.filter(funeral_menu=True)
  
  if(slug == "priyti-pokushat"):
    product = Product.objects.all()
    
  context = {
    "service": service,
    "products": product,
    "categorys": category
  }
  
  if(slug == "pominalnye-obedy"):
    return render(request, "pages/service/service_pominalnye.html", context)
  
  return render(request, "pages/service/service_detail.html", context)