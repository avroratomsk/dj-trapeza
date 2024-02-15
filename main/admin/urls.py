from django.urls import path

from . import views


urlpatterns = [
    path('', views.admin, name="admin"),
    
    #URl - отвечающие за загрузку данных
    path('upload-goods/', views.upload_goods, name="upload_goods"),
    
    #URl - отвечающие за отображение категорий, редактирование и удаление категории
    path('category/', views.admin_category, name='admin_category'),
    path('category/add/', views.category_add, name='category_add'),
    path('category/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),
    
    #URl - отвечающие за отображение дня недели, редактирование и удаление дня недели
    path('days/', views.day_product, name='admin_day'),
    path('days/edit/<int:pk>/', views.day_edit, name='days_edit'),
    path('days/add/', views.day_add, name='days_add'),
    # path('days/delete/<int:pk>/', views.day_delete, name='days_delete'),
    
    #URl - отвечающие за отображение товаров, редактирование и удаление товара
    path('product/', views.admin_product, name='admin_product'),
    path('product/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),
    
    #URl - отвечающие за отображение филлиалов, редактирование и удаление филлиала
    path('fillial/', views.admin_fillial, name='admin_fillial'),
    path('fillial/edit/<int:pk>/', views.fillial_edit, name='fillial_edit'),
    path('fillial/add/', views.fillial_add, name='fillial_add'),
    # path('fillial/delete/<int:pk>/', views.fillial_delete, name='fillial_delete'),
    
    #URl - отвечающие за отображение отзывов, редактирование и удаление отзывов
    path('admin-reviews/', views.admin_reviews, name='admin_reviews'),
    path('admin-reviews/edit/<int:pk>/', views.admin_reviews_edit, name='admin_reviews_edit'),
    # path('admin-reviews/add/', views.admin_reviews_add, name='admin_reviews_add'),
    # path('admin_reviews/delete/<int:pk>/', views.admin_reviews_delete, name='admin_reviews_delete'),
    
    #URl - Шаблон главной страницы
    path('home/', views.admin_home, name='admin_home'),
    
    #URl - Шаблон общих настроек сайта
    path('settings/', views.admin_settings, name='admin_settings'),
]