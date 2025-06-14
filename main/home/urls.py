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
    path('policy/', views.policy, name="policy"),
    path('cookie/', views.cookie, name="cookie"),
    path('callback/', views.callback, name="callback"),
    path('writetous/', views.writetous, name="writetous"),
    path('contacform/', views.contacform, name="contacform"),
    path('consultation/', views.consultation, name="consultation"),
    path('reviewsform/', views.reviewsform, name="reviewsform"),
    path('callback-success/', views.callback_success, name="callback_success"),
    path('', views.index, name="home"),
]