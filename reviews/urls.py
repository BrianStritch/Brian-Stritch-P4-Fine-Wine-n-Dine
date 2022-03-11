from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewsList.as_view(), name='reviews'),
]
