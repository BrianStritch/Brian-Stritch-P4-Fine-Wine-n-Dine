from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.Home.as_view(),
        name='home'
        ),
    path(
        'opening_hours/',
        views.OpeningHours.as_view(),
        name='opening_hours'
        ),
    path(
        'menu/',
        views.Menu.as_view(),
        name='menu'
        ),
    path(
        'products/',
        views.OpeningHours.as_view(),
        name='products'
        ),
    path(
        'about/',
        views.About.as_view(),
        name='about'
        ),
    path(
        'nannys_alternative/sign_up/',
        views.Sign_up.as_view(),
        name='sign_up'
        ),
]
