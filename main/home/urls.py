from django.urls import path, include

from home import views

urlpatterns = [
    path('o-nas/', views.about, name="about" ),
    path('kontakty/', views.contact, name="contact"),
    path('akcii/', views.stock, name="stock"),
    path('akcii/<slug:slug>', views.stock_detail, name="stock_detail"),
    path('gallery/', views.gallery, name="gallery"),
    path('callback/', views.callback, name='callback'),
    path('blog/', include('blog.urls')),
    path('valancies/', views.vacancies, name="vacancies"),
    path('callback/', views.callback, name="callback"),
    path('callback-success/', views.callback_success, name="callback_success"),
    path('', views.index, name="home"),
]