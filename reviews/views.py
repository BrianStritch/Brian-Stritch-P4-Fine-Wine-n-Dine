from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review


class Home(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    queryset = list()
    template_name = 'index.html'
   

class ReviewsList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'reviews.html'
    paginate_by = 8


class ReviewsDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "reviews_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "liked": liked,
            },
        )


class OpeningHours(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'opening-times.html'

  
class AboutPage(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'about.html'

   
class ProductsPage(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'about.html'


class Contact(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'about.html'
    
