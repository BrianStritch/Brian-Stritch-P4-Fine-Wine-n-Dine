from django.urls import path
from . import views
from reviews.views import CreateReview

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('opening_hours/', views.OpeningHours.as_view(), name='opening_hours'),
    path('about/', views.OpeningHours.as_view(), name='about'),
    path('products/', views.OpeningHours.as_view(), name='products'),
    path('contact/', views.OpeningHours.as_view(), name='contact'),
    path('create_review/', views.CreateReview.as_view(), name='create_review'),
    
    path('reviews/', views.ReviewsList.as_view(), name='reviews'),    
    path('<slug:slug>/', views.ReviewsDetail.as_view(), name='review_details'),
    path('like/<slug:slug>/', views.ReviewLike.as_view(), name='review_like'),
]
