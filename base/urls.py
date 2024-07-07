from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home),
    path('search', views.getUser),
    path('add', views.add)
]