from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q, Count
from django.core.exceptions import ObjectDoesNotExist
from shop.models import Category, Product
from service.models import Service, ServiceCategory, ServicePage, ServiceProduct
import json
from django.http import JsonResponse

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
  
  category = ServiceCategory.objects.all()
  if request.path != "/service/pominalnye-obedy/":
    try:
      product = ServiceProduct.objects.filter(service=service, category_id=1)
    except:
      pass
  else:
    try:
      product = ServiceProduct.objects.filter(service=service)
    except:
      pass
  
  context = {
    "service": service,
    "products": product,
    "categorys": category,
  }
  
  if request.path == "/service/pominalnye-obedy/":
    return render(request, "pages/service/service_pominalnye.html", context)
  else:
    return render(request, "pages/service/service_detail.html", context)
  
def get_data_service(request):
    data = json.loads(request.body)
    category_id = data.get('category_id')
    products = ServiceProduct.objects.filter(category_id=category_id)
    data = []
      
    for product in products:
      try:
        product_image = product.image.url
      except:
        product_image = '/core/theme/mb/images/no-image.jpg'
      
      try: 
        product_price = product.price
      except:
        product_price = "Не указана"
        
      data.append({
        'name': product.name,
        'price': product_price,
        'image': product_image
      })
    return JsonResponse({"data": data})
    


