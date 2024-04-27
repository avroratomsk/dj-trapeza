from django.urls import path

from service import views


urlpatterns = [
    path('', views.service, name="service"),
    path('get_data_service/', views.get_data_service, name="get_data_service"),
    path('<slug:slug>/', views.service_detail, name="service_detail"),
    path('category/<slug:slug>/', views.service_detail, name="service_product_category"),
]