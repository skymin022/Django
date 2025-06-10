from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event-popup/', views.event_popup, name='event_popup')
]