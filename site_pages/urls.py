from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('opening_hours/', views.OpeningHours.as_view(), name='opening_hours'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('products/', views.OpeningHours.as_view(), name='products'),
    path('contact/', views.OpeningHours.as_view(), name='contact'),
    path('nannys_alternative/account_details/', views.User_account_details.as_view(), name='user_account'),
]
    