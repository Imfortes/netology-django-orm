from django.urls import path

from . import views

urlpatterns = [
    path('', views.phones_magazine, name='phones_magazine'),
    path('<slug:slug>/', views.phone_detail, name='phone_detail'),
]