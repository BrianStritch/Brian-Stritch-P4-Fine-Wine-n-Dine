from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.views import generic, View 
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Review, Comment
from .forms import CommentForm, CreateReviewForm 


class ReviewsList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'reviews/reviews.html'
    paginate_by = 8

class CreateReview(TemplateView):
    template_name = 'reviews/create_review.html'
    
    
    def get(self, request):
        form = CreateReviewForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateReviewForm(request.POST)        
        
        if form.is_valid():
            form.instance.email = request.user.email
            email = form.instance.email
            form.instance.name = request.user.username
            name = form.instance.name
            form.instance.author = request.user
            title = form.cleaned_data['title']
            form.instance.slug = slugify(title)
            content = form.cleaned_data['content']
            featured_image = form.cleaned_data['featured_image']
            excerpt = form.cleaned_data['excerpt'] 
            review = form.save(commit=False)
            review.post = review
            review.save()
        else:
            form = CreateReviewForm()

        return HttpResponseRedirect(reverse('reviews'))


class EditReview(UpdateView):
    model = Review
    template_name = 'reviews/edit_review.html'
    fields = [
        'title',
        'content',
        'featured_image',
        'excerpt',
        ]

class DeleteReview(DeleteView):
    model = Review
    template_name = 'reviews/delete_review.html'
    success_url = reverse_lazy('reviews')


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
            "reviews/reviews_detail.html",
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
            "reviews/reviews_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                'comment_form': CommentForm(),
            },
        )

class EditComment(UpdateView):
    model = Comment
    template_name = 'reviews/edit_comment.html'
    fields = [
        'body',
        ]

class DeleteComment(DeleteView):
    model = Comment
    template_name = 'reviews/delete_comment.html'
    success_url = reverse_lazy('reviews')


class ReviewLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Review, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('review_details', args=[slug]))



