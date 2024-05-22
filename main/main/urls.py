from django.urls import path,include
from django.conf.urls.static import static
from django.contrib import admin

from main import settings
from shop import views

urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    # path('admin/', admin.site.urls),
    path('about/', include('home.urls')),
    path('catalog/', include('shop.urls')),
    path('service/', include('service.urls')),
    path('blog/', include('blog.urls')),
    path('news/', include('news.urls')),
    # path('user/', include('users.urls')),
    path('reviews/', include('reviews.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', include('admin.urls')),
    path('', include('home.urls')),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)