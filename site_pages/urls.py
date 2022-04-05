"""
    imports  -------------site_pages urls.py----------------------
"""
# third party imports
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
        'gallery/',
        views.Gallery.as_view(),
        name='gallery'
        ),
    path(
        'about/',
        views.About.as_view(),
        name='about'
        ),
    path(
        'sign_up_now/',
        views.SignUp.as_view(),
        name='sign_up'
        ),
    path(
        'profile/',
        views.Profile.as_view(),
        name='profile'
        ),
    path(
        'edit_profile/',
        views.EditProfile.as_view(),
        name='edit_profile'
        ),
    path(
        'delete_profile/<int:pk>/',
        views.DeleteProfile.as_view(),
        name='delete_profile'
        ),
]
