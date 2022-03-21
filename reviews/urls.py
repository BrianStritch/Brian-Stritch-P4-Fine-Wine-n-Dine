from django.urls import path
from . import views
from reviews.views import CreateReview, EditReview

urlpatterns = [    
    path('reviews/create_review/', views.CreateReview.as_view(), name='create_review'),        
    path('reviews/reviews/', views.ReviewsList.as_view(), name='reviews'),    
    path('reviews/<slug:slug>/', views.ReviewsDetail.as_view(), name='review_details'),
    path('reviews/like/<slug:slug>/', views.ReviewLike.as_view(), name='review_like'),
    path('reviews/edit_review/<slug:slug>/', views.EditReview.as_view(), name='edit_review'), 
    path('reviews/edit_comment/<int:id>', views.EditComment.as_view(), name='edit_comment'), 
]