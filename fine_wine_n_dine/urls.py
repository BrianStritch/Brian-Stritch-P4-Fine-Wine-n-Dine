"""
fine_wine_n_dine URL Configuration
 
"""
from django.contrib import admin
from django.urls import path, include
from reviews import views
from bookings import views
from site_pages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('sign_up/', include('site_pages.urls'), name='sign_up'),
    path('reviews/', include('reviews.urls'), name='reviews'),
    path('bookings/', include('bookings.urls'), name='bookings'),
    path('accounts/', include('allauth.urls')),    
    path('', include('site_pages.urls'), name='home'),
        
]
