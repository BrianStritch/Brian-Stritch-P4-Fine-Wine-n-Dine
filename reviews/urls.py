from . import views
from django.urls import path

urlpatterns = [
    path('',  views.ReviewsList.as_view(), name='reviews'),
    
]
