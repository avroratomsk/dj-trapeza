from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q, Count
from django.core.exceptions import ObjectDoesNotExist
from shop.models import Category, Product
from service.models import Service, ServiceCategory, ServicePage, ServiceProduct

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
  category = ServiceCategory.objects.all()
  service = Service.objects.get(slug=slug)
  product = ServiceProduct.objects.filter(service=service)
  categories_with_products = Service.objects.annotate(num_products=Count('serviceproduct')).filter(num_products__gt=0)
  
  context = {
    "service": service,
    "products": product,
    "categorys": category,
  }
  
  return render(request, "pages/service/service_detail.html", context)

