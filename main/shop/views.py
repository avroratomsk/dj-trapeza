import json
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q

from .services import *


from .models import *

def catalog(request):
  category = Categories.objects.all()
  
  context = {
    "title": "Заголовок категорий",
    "category": category,
  }

  return render(request, "pages/catalog/products.html", context)



def category_detail(request, slug=None):
  # Получаем из GET параметра page для пагинации
  page = request.GET.get("page", 1)
  
  category_name = get_object_or_404(Categories, slug=slug)
  
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
    "category": Categories.objects.all(),
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
@csrf_exempt
def get_product(request,):
  if request.method == 'POST':
      data = json.loads(request.body)
      branch_id = data.get('branch_id')
      print(branch_id)
      products = Product.objects.filter(subsidiary__id=branch_id)
      print(products)
      product_list = '<ul>'
      for product in products:
          product_url = request.build_absolute_uri(reverse('product', kwargs={'slug': product.slug}))
          product_list += f'<li><a href="{product_url}">{product.name} - {product.price}</a></li>'
      product_list += '</ul>'
      return HttpResponse(product_list)
  return HttpResponse(status=400)
    