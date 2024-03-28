from django.urls import path

from home import views

urlpatterns = [
    path('o-nas/', views.about, name="about"),
    path('kontakty/', views.contact, name="contact"),
    path('akcii/', views.stock, name="stock"),
    path('akcii/<slug:slug>', views.stock_detail, name="stock_detail"),
    path('gallery/', views.gallery, name="gallery"),
    path('blog/', views.about, name="about"),
    # path('valancy/', views.about, name="about"),
    
    path('', views.index, name="home"),
]