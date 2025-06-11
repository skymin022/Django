from django.urls import path
# from .views import create_view, list_view, read_view, update_view
from .views import *

# 앱 이름 설정
app_name = 'post'


urlpatterns = [
    path('create/', create_view, name='create'),
    path('list/', list_view, name='list'),
    path('<int:post_id>', read_view, name='read'),
    path('update/<int:post_id>', update_view, name='update'),
    path('delete/<int:post_id>', delete_view, name='delete'),
]