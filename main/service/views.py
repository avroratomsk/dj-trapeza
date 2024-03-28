from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q

from shop.models import Category, Product
from service.models import Service

def service(request):
  services = Service.objects.filter(status=True)
  
  context = {
    "services": services
  }
  return render(request, "pages/service/service.html", context)

def service_detail(request, slug):
  category = Category.objects.all()
  service = Service.objects.get(slug=slug)
  if(slug == "organizovat-banket"):
    product = Product.objects.filter(banquet_menu_checkbox=True)
  
  if(slug == "pominalnye-obedy"):
    product = Product.objects.filter(funeral_menu=True)
  
  if(slug == "priyti-pokushat"):
    product = Product.objects.all()
    
  context = {
    "service": service,
    "products": product,
    "categorys": category
  }
  
  return render(request, "pages/service/service_detail.html", context)