from django.shortcuts import render
from django.views import generic
from .models import Review

class ReviewsList(generic.ListView):    
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'reviews.html'
    paginate_by = 8


