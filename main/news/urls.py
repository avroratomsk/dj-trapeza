from django.urls import path

from news import views

urlpatterns = [
    path('', views.news, name="news"),
    path('<slug:slug>/', views.new, name="new"),
]