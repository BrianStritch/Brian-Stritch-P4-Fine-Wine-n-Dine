from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.views import generic, View 
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Review
from .forms import CommentForm, CreateReviewForm



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
                'comment_form': CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = review
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "reviews_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                'comment_form': CommentForm(),
            },
        )


class ReviewLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Review, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('review_details', args=[slug]))









# class CreateReview(View):

#     def get(self, request, *args, **kwargs):        
#         form = CreateReviewForm()
#         context = {'form': form }
#         return render(request, 'create_review.html', context)

# class SaveNewReview(View):
    
#     def post(self, request, slug=None, *args, **kwargs):
#         form = CreateReviewForm(request.POST)
#         new_review = get_object_or_404(Review, slug=slug)
#         current_user = User

#         if form.is_valid():            
#             form.instance.email = request.user.email
#             form.instance.name = request.user.username
#             new_review.author = request.user.username
#             user.id = current_user.id
#             if form.instance.featured_image == '':
#                 featured_image = "placeholder"
#             new_review = form.save(commit=False)           
#             new_review.save()
#         else:
#             form = CreateReviewForm()
            
        
#         return HttpResponseRedirect(reverse('reviews', args=[slug]))



        




# class CreateNewReview(View):
#     model = Review
#     queryset = list()

#     def post(self, request, *args, **kwargs):
#         review = get_object_or_404(Review)
#         review_form = ReviewForm(data=request.POST)

#         if review_form.is_valid():
            
"""
test new review form 
"""       


class CreateReview(TemplateView):
    template_name = 'create_review.html'
    
    
    def get(self, request):
        form = CreateReviewForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateReviewForm(request.POST)        
        
        if form.is_valid():
            form.instance.email = request.user.email
            email = form.instance.email
            form.instance.name = request.user.username
            name = form.instance.name
            
            #author = form.instance.author

            title = form.cleaned_data['title']
            form.instance.slug = slugify(title)
            content = form.cleaned_data['content']
            featured_image = form.cleaned_data['featured_image']
            excerpt = form.cleaned_data['excerpt'] 

            review = form.save(commit=False)
            #review.user = request.user
            #form.instance.author = review.user.id
            review.post = review
            review.save()
        else:
            form = CreateReviewForm()

        return HttpResponseRedirect(reverse('reviews'))
       

            
            
    
    
    
    
    
    
    
    # def post(self, request):
    #     #queryset = Review.objects.filter(status=1)
    #     review = get_object_or_404(queryset)
    #     comments = review.comments.filter(approved=True).order_by('created_on')
    #     liked = False
    #     if review.likes.filter(id=self.request.user.id).exists():
    #         liked = True
        
    #     comment_form = ReviewForm(data=request.POST)

    #     if comment_form.is_valid():
    #         comment_form.instance.email = request.user.email
    #         comment_form.instance.name = request.user.username
    #         comment = comment_form.save(commit=False)
    #         comment.post = review
    #         comment.save()
    #     else:
    #         comment_form = ReviewForm()

        # return render(
        #     request,
        #     "reviews_detail.html",
        #     {
        #         "review": review,
        #         "comments": comments,
        #         "commented": True,
        #         "liked": liked,
        #         'comment_form': ReviewForm(),
        #     },
        # )

        
 # return render(
        #     request, 
        #     self.template_name, 
        #     context = {
        #         #'form': form, 
        #         'title': title,                 
        #         'content': content, 
        #         'featured_image': featured_image, 
        #         'excerpt': excerpt,
        #         'email': email,
        #         'name': name,
        #         'new_review': True,                
        #         #'id': id,               
                
        #         }  )
"""
end test
"""
































































class Menu(TemplateView):
    template_name = 'menu.html'


class OpeningHours(TemplateView):
    template_name = 'opening-times.html'

   
class ProductsPage(TemplateView):
    template_name = 'about.html'


class Contact(TemplateView):
    template_name = 'about.html'
    
