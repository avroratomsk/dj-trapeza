from django.urls import path, include

from home import views

urlpatterns = [
    path('o-nas/', include('blog.urls')),
    path('kontakty/', views.contact, name="contact"),
    path('akcii/', views.stock, name="stock"),
    path('akcii/<slug:slug>', views.stock_detail, name="stock_detail"),
    path('gallery/', views.gallery, name="gallery"),
    path('callback/', views.callback, name='callback'),
    # path('blog/', views.about, name="about"),
    path('valancies/', views.vacancies, name="vacancies"),
    
    path('', views.index, name="home"),
]