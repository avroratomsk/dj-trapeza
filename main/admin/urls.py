from django.urls import path

from . import views


urlpatterns = [
    path('', views.admin, name="admin"),
    
    #URl - отвечающие за загрузку данных
    path('upload-goods/', views.upload_goods, name="upload_goods"),
    path('upload-succes/', views.upload_succes, name="upload-succes"),
    
    #URl - отвечающие за отображение категорий, редактирование и удаление категории
    path('category/', views.admin_category, name='admin_category'),
    path('category/add/', views.category_add, name='category_add'),
    path('category/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),
    
    #URl - отвечающие за отображение дня недели, редактирование и удаление дня недели
    path('days/', views.day_product, name='admin_day'),
    path('days/add/', views.day_add, name='days_add'),
    path('days/edit/<int:pk>/', views.day_edit, name='days_edit'),
    # path('days/delete/<int:pk>/', views.day_delete, name='days_delete'),
    
    #URl - отвечающие за отображение товаров, редактирование и удаление товара
    path('product/', views.admin_product, name='admin_product'),
    path('product/<int:id>/', views.admin_product_category, name='admin_product_category'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('product/edit_day/<int:id>/', views.product_day_edit, name='product_day_edit'),
    
    #URl - отвечающие за отображение филлиалов, редактирование и удаление филлиала
    path('fillial/', views.admin_fillial, name='admin_fillial'),
    path('fillial/add/', views.fillial_add, name='fillial_add'),
    path('fillial/edit/<int:pk>/', views.fillial_edit, name='fillial_edit'),
    # path('fillial/delete/<int:pk>/', views.fillial_delete, name='fillial_delete'),
    
    #URl - отвечающие за отображение отзывов, редактирование и удаление отзывов
    path('admin-reviews/', views.admin_reviews, name='admin_reviews'),
    path('admin-reviews/add/', views.admin_reviews_add, name='admin_reviews_add'),
    path('admin-reviews/edit/<int:pk>/', views.admin_reviews_edit, name='admin_reviews_edit'),
    # path('admin_reviews/delete/<int:pk>/', views.admin_reviews_delete, name='admin_reviews_delete'),
    
    #URl - отвечающие за отображение акций, редактирование и удаление акций
    path('stock-settings/', views.stock_settings, name='stock_settings'),
    path('stock/', views.admin_stock, name='admin_stock'),
    path('stock/add/', views.stock_add, name='stock_add'),
    path('stock/edit/<int:pk>/', views.stock_edit, name='stock_edit'),
    path('stock/delete/<int:pk>/', views.stock_delete, name='stock_delete'),
    
    #URl - отвечающие за отображение галлереи, редактирование и удаление фотографий галлереи
    path('gallery-settings/', views.admin_gallery_settings, name='gallery_settings'),
    path('gallery/', views.admin_gallery, name='admin_gallery'),
    path('gallery/add/', views.gallery_add, name='gallery_add'),
    path('gallery/edit/<int:pk>/', views.gallery_edit, name='gallery_edit'),
    path('gallery/delete/<int:pk>/', views.gallery_delete, name='gallery_delete'),
    
    #URl - отвечающие за отображение услуг, редактирование и удаление услуг
    path('serv-product/', views.service_product, name='service_product'),
    path('serv-product/add/', views.service_product_add, name='service_product_add'),
    path('serv-product/edit/<int:pk>/', views.service_product_edit, name='service_product_edit'),
    path('serv-product/delete/<int:pk>/', views.service_product_delete, name='service_product_delete'),
    
    path('serv-category/', views.service_category, name='service_category'),
    path('serv-category/add/', views.service_category_add, name='service_category_add'),
    path('serv-category/edit/<int:pk>/', views.service_category_edit, name='service_category_edit'),
    # path('serv-category/delete/<int:pk>/', views.service_category_delete, name='service_category_delete'),
    
    path('serv-page/', views.service_page, name='service_page'),
    path('serv/', views.admin_service, name='admin_service'),
    path('serv/add/', views.service_add, name='service_add'),
    path('serv/edit/<int:pk>/', views.service_edit, name='service_edit'),
    path('serv/delete/<int:pk>/', views.service_delete, name='service_delete'),
    
    #URl - отвечающие за отображение статей, редактирование и удаление статей
    path('blog-settings/', views.blog_settings, name='blog_settings'),
    path('blog/', views.admin_blog, name='admin_blog'),
    path('blog/add/', views.blog_add, name='post_add'),
    path('blog/edit/<int:pk>/', views.blog_edit, name='post_edit'),
    path('blog/delete/<int:pk>/', views.blog_delete, name='post_delete'),
    
    #URl - отвечающие за отображение новостей, редактирование и удаление новостей
    path('news-settings/', views.news_settings, name='news_settings'),
    path('news-admin/', views.admin_news, name='admin_news'),
    path('news/add/', views.news_add, name='news_add'),
    path('news/edit/<int:pk>/', views.news_edit, name='news_edit'),
    path('news/delete/<int:pk>/', views.news_delete, name='news_delete'),
    
    #URl - Шаблон главной страницы
    path('home/', views.admin_home, name='admin_home'),
    path('about/', views.admin_about, name='admin_about'),
    path('blog-page/', views.blog_page, name='blog_page'),
    path('pomin/', views.pomin_page, name='pomin_page'),
    path('banket/', views.banket_page, name='banket_page'),
    
    #URl - Шаблон общих настроек сайта
    path('settings/', views.admin_settings, name='admin_settings'),
    
    path('shop/', views.admin_shop, name='admin_shop'),
    path('vacancy/', views.admin_vacancy, name='admin_vacancy'),
    path('vacancys/', views.vacancys, name='vacancys'),
    path('vacancys/add/', views.vacancy_add, name='vacancy_add'),
    path('vacancys/edit/<int:pk>', views.vacancy_edit, name='vacancy_edit'),
    path('vacancys/delete/<int:pk>', views.vacancy_delete, name='vacancy_delete'),
    
    #URl - настройка цветовой схемы на сайте
    path('design/', views.admin_colors, name='admin_colors'),
]