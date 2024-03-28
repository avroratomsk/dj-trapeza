from django.urls import path

from shop import views


urlpatterns = [
    # path('search/', views.category_detail, name="search"),
    path('', views.catalog, name="catalog"),
    path('get_data/', views.get_data, name="get_data"),
    path('get-product/',views.get_products, name="get_products"),
    #Если я сделаю данный маршрут ниже чем catalog_detail, то поиск не будет работать по той причине что всегда будет выаолняться маршрут в который передали slug
    path('<slug:slug>/', views.category_detail, name="category_detail"),
    path('product/<slug:slug>/', views.product, name="product"),
]