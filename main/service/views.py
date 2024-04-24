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
    pass
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
  products = ServiceProduct.objects.filter(service_id=service).prefetch_related('category')
  products_by_category = {}
  
  for category in category:
      products_by_category[category] = [product for product in products if product.category == category]
  
  
  context = {
    "service": service,
    "products": product,
    "categorys": category,
    "product_category": products_by_category,
    'products_by_category': products_by_category
  }
  if request.path == "/service/pominalnye-obedy/":
    return render(request, "pages/service/service_pominalnye.html", context)
  else:
    return render(request, "pages/service/service_detail.html", context)
    

