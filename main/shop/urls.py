from django.urls import path

from shop import views


urlpatterns = [
    path('search/', views.category_detail, name="search"), 
    path('', views.catalog, name="catalog"),
    path('<int:category_id>',views.get_category_products, name="get_category_products"),
    #Если я сделаю данный маршрут ниже чем catalog_detail, то поиск не будет работать по той причине что всегда будет выаолняться маршрут в который передали slug
    path('<slug:slug>/', views.category_detail, name="category_detail"),
    path('get_product/', views.get_product, name="get_product"),
    path('product/<slug:slug>/', views.product, name="product"),
]