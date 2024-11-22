import json
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q
from PIL import Image
import io
import os
from .services import *
import datetime
from django.http import JsonResponse


from .models import *

def catalog(request):
  category = Category.objects.all()
  
  context = {
    "title": "Заголовок категорий",
    "category": category,
  }

  return render(request, "pages/catalog/products.html", context)



# def get_category_products(request, category_id):
#   # Получаем текущую дату
#   current_date = datetime.datetime.now()

#   # Получаем номер дня недели (0 для понедельника, 1 для вторника и т.д.)
#   day_of_week = current_date.weekday()
#   products = Product.objects.filter(day=day_of_week, category_id=category_id)
#   print(products)
#   data = []
#   for product in products:
#     data.append({
#       'name': product.name,
#       'price': product.price,
#       'url': product.get_absolute_url(), # URL детальной страницы продукта
#       'image': "None"
#     })
  
#   context = {
#     "data": data
#   }
#   return render(request, 'pages/index.html', context)
#   # return JsonResponse({"data": data})

def get_category_products(request, category_id):
  # Получаем текущую дату
  current_date = datetime.datetime.now()

  # Получаем номер дня недели (0 для понедельника, 1 для вторника и т.д.)
  day_of_week = current_date.weekday()
  products = Product.objects.filter(day=day_of_week, category_id=category_id)
  print(products)
  data = []
  for product in products:
    data.append({
      'name': product.name,
      'price': product.price,
      'url': product.get_absolute_url(), # URL детальной страницы продукта
      'image': "None"
    })
  
  context = {
    "data": data
  }
  return render(request, 'pages/index.html', context)



def get_data(request):
    current_date = datetime.datetime.now()
    # Получаем номер дня недели (0 для понедельника, 1 для вторника и т.д.)
    day_of_week = current_date.weekday()
    data = json.loads(request.body)
    category_id = data.get('category_id')
    branch_slug = data.get('branch_slug')
    branch = Branch.objects.get(slug=branch_slug)
    branch_info = [branch.name, branch.image.url, branch.phone, branch.address_fillial, branch.time_work, branch.weekend, branch.map_code]
    products = Product.objects.filter(branch=branch, category_id=category_id, day=day_of_week)
    data = []
      
    for product in products:
      try:
        image  = product.image.url
      except:
        image = "/core/theme/mb/images/no-image.png"
        
      data.append({
        'name': product.name,
        'price': product.price,
        'price_two': product.price_two,
        'weight': product.weight,
        'weight_two': product.weight_two,
        'url': product.get_absolute_url(), # URL детальной страницы продукта
        'image': image
      })
      # print(data)
    return JsonResponse({"data": data, "branch": branch_info})


def get_products(request, id):
  product = Product.objects.filter(category_id=id)
  print(product)
  
  return JsonResponse({"product": product})

def category_detail(request, slug=None):
  # Получаем из GET параметра page для пагинации
  page = request.GET.get("page", 1)
  
  category_name = get_object_or_404(Category, slug=slug)
  
  products = Product.objects.filter(category__slug=slug)
  
  paginator = Paginator(products, 15)
  current_page = paginator.page(int(page))
  
  context = {
    "current_slug": slug,
    "category_name": category_name,
    "products": current_page,
    "category": Category.objects.all(),
  }
  
  return render(request, "pages/catalog/single.html", context)

def product(request, slug):
  product = get_object_or_404(Product, slug=slug)
  category = Category.objects.all()
  # products = Product.objects.filter(~Q(slug=slug), category__pk=product.category.id)
  try:
    products = Product.objects.filter(category__pk=product.category.id).exclude(slug=slug)[:8]
  except:
    pass
    
  
  context = {
    "categorys":category,
    "products": products,
    "product": product,
    "prod_slug": slug,
  }
  return render(request, "pages/catalog/view-product.html", context)


# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile


@csrf_exempt
def get_category_products(request):
    if request.method == 'POST':
        category_id = int(request.POST.get('category_id'))
        products = Product.objects.filter(category_id=category_id).values('name')
        
        return JsonResponse({'products': list(products)})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    