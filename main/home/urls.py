from django.urls import path

from home import views

urlpatterns = [
    path('o-nas/', views.about, name="about"),
    path('kontakty/', views.contact, name="contact"),
    path('akcii/', views.stock, name="stock"),
    path('katalog/', views.about, name="about"),
    path('uslugi/', views.about, name="about"),
    path('valancy/', views.about, name="about"),
    
    path('', views.index, name="home"),
]