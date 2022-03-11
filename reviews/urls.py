from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),    
    path('reviews/', views.ReviewsList.as_view(), name='reviews'),
    path('reviews/<slug:slug>/', views.ReviewsDetail.as_view(), name='reviews_detail'),
    path('opening_hours/', views.OpeningHours.as_view(), name='opening_hours'),
    path('about/', views.OpeningHours.as_view(), name='about'),
    path('products/', views.OpeningHours.as_view(), name='products'),
    path('contact/', views.OpeningHours.as_view(), name='contact'),
]
