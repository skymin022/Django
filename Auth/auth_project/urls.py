from django.contrib import admin
from django.urls import path, include
from post.views import index

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('post/', include('post.urls')),
    path('admin/', admin.site.urls),
]
