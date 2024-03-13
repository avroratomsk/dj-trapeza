import json
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q
from PIL import Image
import io
import os
from .services import *


from .models import *

def catalog(request):
  category = Category.objects.all()
  
  context = {
    "title": "Заголовок категорий",
    "category": category,
  }

  return render(request, "pages/catalog/products.html", context)

def resize_image(image_path, width, height):
  print(image_path)
  if not os.path.exists(image_path):
    print(f"File does not exist.")
    return None
  try:
    img = Image.open(image_path)
    img.thumbnail((width, height))

    output = io.BytesIO()
    img.save(output, format='JPG')
    print(f"{output.getvalue()} - Первое")
    return output.getvalue()
  except Exception as e:
    print(f"Error processing image: {e}")
    return None

def get_category_products(request, category_id):
  current_day = Day.objects.get(num_day=datetime.today().weekday())
  products = Product.objects.filter(day__id=current_day.id, category_id=category_id)
  print(products)
  data = []
  for product in products:
    data.append({
      'name': product.name,
      'price': product.price,
      'url': product.get_absolute_url(), # URL детальной страницы продукта
      'image': "None"
    })
  return JsonResponse({"data": data})

def category_detail(request, slug=None):
  # Получаем из GET параметра page для пагинации
  page = request.GET.get("page", 1)
  
  category_name = get_object_or_404(Category, slug=slug)
  
  # Получаем текущий день из таблицы Day
  current_day = Day.objects.get(num_day=datetime.today().weekday())
 
  # Получаем выбранный день из GET параметра day
  selected_day = request.GET.get("day", None)
  
  # Делаем проверку и в зависимости от действий пользователя выводить продукцию
  if selected_day:
    products = Product.objects.filter(Q(day__slug=selected_day) | Q(day__slug="all_days"), category__slug=slug)
  else:
    products = Product.objects.filter(Q(day__id=current_day.id) | Q(day__slug="all_days"), category__slug=slug)
  
  paginator = Paginator(products, 15)
  current_page = paginator.page(int(page))
  current_slug = request.GET.get("slug")
  
  context = {
    "current_slug": slug,
    "category_name": category_name,
    "products": current_page,
    "category": Category.objects.all(),
  }
  
  return render(request, "pages/catalog/single.html", context)

def product(request, slug):
  product = get_object_or_404(Product, slug=slug)
  # products = Product.objects.filter(~Q(slug=slug), category__pk=product.category.id)
  products = Product.objects.filter(category__pk=product.category.id).exclude(slug=slug)
  
  context = {
    "products": products,
    "product": product,
    "prod_slug": slug,
  }
  return render(request, "pages/catalog/view-product.html", context)

from django.http import JsonResponse
# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
@csrf_exempt
def get_product(request):
  if request.method == 'POST':
      data = json.loads(request.body)
      branch_id = data.get('branch_id')
      products = Product.objects.filter(subsidiary__id=branch_id)
      product_list = '<div>'
      for product in products:
            product_url = request.build_absolute_uri(reverse('product', kwargs={'slug': product.slug}))
            product_list += f'<li><a href="{product_url}">{product.name} - {product.price}<br></a></li>'
      product_list += '</div>'
      return HttpResponse(product_list)
  return HttpResponse(status=400)
    