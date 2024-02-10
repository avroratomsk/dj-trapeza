from django.urls import path

from home import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('contact/', views.about, name="about"),
    path('stock/', views.about, name="about"),
    path('menu/', views.about, name="about"),
    path('service/', views.about, name="about"),
    path('valancy/', views.about, name="about"),
    
    path('', views.index, name="home"),
]