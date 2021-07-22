
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
     path('title/<str:menu>/', views.detail)
]

