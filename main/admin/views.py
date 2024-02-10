import xlrd

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from admin.forms import CategoryForm, DayForm, ProductForm
from shop.models import Product,Categories,Day
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
# from django.contrib.auth.decorators import user_passes_test

# @user_passes_test(lambda u: u.is_superuser)
# def sidebar_show(request): 
   
#     request.session['sidebar'] = 'True' 
    
#     return redirect('admin')

# @user_passes_test(lambda u: u.is_superuser)

def admin(request):
  """Данная предстовление отобразает главную страницу админ панели"""
  return render(request, "page/index.html")

def admin_product(request):
  """
  View, которая возвращаяет и отрисовывает все товары на странице
  и разбивает их на пагинацию 
  """
  page = request.GET.get('page', 1)
  
  products = Product.objects.all()
  paginator = Paginator(products, 10)
  current_page = paginator.page(int(page))
  
  context = {
    "products": current_page
  }
  return render(request, "shop/product/product.html", context)


def product_edit(request, pk):
  """
    View, которая получает данные из формы редактирования товара
    и изменяет данные внесенные данные товара в базе данных
  """
  product = Product.objects.get(id=pk)
  form = ProductForm(instance=product)
  
  form_new = ProductForm(request.POST, request.FILES, instance=product) 
  if request.method == 'POST':
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_product')
    else:
      return render(request, 'shop/product/product_edit.html', {'form': form_new,})
  context = {
    "form":form
  }
  return render(request, "shop/product/product_edit.html", context)

def product_add(request):
  form = ProductForm()
  
  if request.method == "POST":
    form_new = ProductForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_product')
    else:
      return render(request, "shop/product/product_add.html", {"form": form_new})
    
  context = {
    "form": form
  }
  
  return render(request, 'shop/product/product_add.html', context)

def product_delete(request,pk):
  product = Product.objects.get(id=pk)
  product.delete()
  
  return redirect('admin_product')

class UploadingProducts(object):
  # prod = Product.objects.all()
  # prod.delete()
  
  foreign_key_fields = ["category","day"]
  model = Product
  
  
  def __init__(self, data):
    data = data
    self.uploaded_file = data.get("file")
    self.parsing()
    
  def getting_related_model(self, field_name):
    related_model = self.model._meta.get_field(field_name).remote_field.model
    return related_model
  
  def getting_headers(self):
    s = self.s 
    headers = dict()
    for column in range(s.ncols):
      value = s.cell(0, column).value
      headers[column] = value
    return headers
  
  def parsing(self):
    uploaded_file = self.uploaded_file
    wb = xlrd.open_workbook(file_contents=uploaded_file.read())
    s = wb.sheet_by_index(0)
    self.s = s
    
    headers = self.getting_headers()
    print(f"{headers} -  Заголовки")
    
    product_bulk_list = list()
    for row in range(1, s.nrows):
      row_dict = {}
      for column in range(s.ncols):
        value = s.cell(row,column).value
        field_name = headers[column]
        
        if field_name == "id" and not value:
          continue
        
        if field_name == "date" and not value:
          continue
        
        if field_name in self.foreign_key_fields:
          related_model = self.getting_related_model(field_name)
          print(related_model)
          
          isinstance, created = related_model.objects.get_or_create(name=value)
          value = isinstance
        row_dict[field_name] = value
      
      print(row_dict)
      # product_bulk_list.append(Product(**row_dict))
      Product.objects.create(**row_dict)
    
    # Product.objects.bulk_create(product_bulk_list)
    # return True

def upload_goods(request):
  if request.POST:
    print(request.POST)
    print(request.FILES)
    file = request.FILES['upload_file']
    uploading_file = UploadingProducts({"file": file})
    if uploading_file:
      print('Успешная загрузка')
    else:
      print('Ошибка загрузки файла')
  else:
    print("Не метод POST")
      
  return render(request, "upload/upload.html")


def admin_category(request):
  categorys = Categories.objects.all()
  
  context ={
    "categorys": categorys,
  }
  return render(request, "shop/category/category.html", context)

def category_add(request):
  form = CategoryForm()
  if request.method == "POST":
    form_new = CategoryForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_category")
    else:
      return render(request, "shop/category/category_add.html", {"form": form_new})
    
  context = {
    "form": form
  }
  return render(request, "shop/category/category_add.html", context)

def category_edit(request, pk):
  categorys = Categories.objects.get(id=pk)
  if request.method == "POST":
    form = CategoryForm(request.POST, request.FILES, instance=categorys)
    if form.is_valid():
      form.save()
      return redirect("admin_category")
    else:
      return render(request, "shop/category/category_edit.html", {"form": form})
  
  context = {
    "form": CategoryForm(instance=categorys),
    "categorys": categorys
  }

  return render(request, "shop/category/category_edit.html", context)

def category_delete(request, pk):
  category = Categories.objects.get(id=pk)
  category.delete()
  
  return redirect('admin_category')

def day_product(request):
  days = Day.objects.all()
  
  context = {
    "days": days,
  }
  
  return render(request, "days/days.html", context)

def day_edit(request, pk):
  day = Day.objects.get(id=pk)
  form = DayForm(instance=day)
  
  if request.method == "POST":
    form_new = DayForm(request.POST)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin_day")
    else:
      return render(request, "days/days_edit.html", {"form": form_new})

  context = {
    "form": form,
  }
  
  return render(request, "days/days_edit.html", context)

