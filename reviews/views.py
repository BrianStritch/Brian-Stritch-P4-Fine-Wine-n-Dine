"""
    imports  ------Reviews views.py----------------------
"""
# third party imports
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# internal imports
from .models import Review, Comment
from .forms import CommentForm, CreateReviewForm


class ReviewsList(generic.ListView):
    """
        Class based view to display all reviews
    """
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'reviews/reviews.html'
    paginate_by = 9


class CreateReview(TemplateView):
    """
        Class based view to render create reviews page
        with CreateReviewForm to create new reviews, GET request
        data from user and process POST request accordingly
    """
    template_name = 'reviews/create_review.html'

    def get(self, request, *args, **kwargs):
        """
        GET request for rendering the create review
        page including the CreateReviewForm
        """
        form = CreateReviewForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        POST request for processing the CreateReviewForm
        data passed from the create review page and if
        form is valid saves booking to database.
        """
        form = CreateReviewForm(request.POST)
        if form.is_valid():
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
            return render(request, self.template_name, {'form': form})

        return HttpResponseRedirect(reverse('reviews'))


class EditReview(UpdateView):
    """
        Class based view to display edit booking
        page with booking form relative to the
        current selected booking and utilising
        the built in django updateview for saving
        updated data to the database.
    """
    model = Review
    template_name = 'reviews/edit_review.html'
    fields = [
        'title',
        'content',
        'featured_image',
        'excerpt',
        ]


class DeleteReview(DeleteView):
    """
        Class based view to delete the selected
        review using the built in Django Deleteview.
    """
    model = Review
    template_name = 'reviews/delete_review.html'
    success_url = reverse_lazy('reviews')


class ReviewsDetail(View):
    """
        Class based view to display the selected
        reviews specific details and comments.
    """
    template_name = "reviews/reviews_detail.html"

    def get(self, request, slug):
        """
        class based function to render the reviews detail page
        diaplaying the review details for the selected review
        and renders the commentform and displays all comments
        related to the specific review.
        """
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            self.template_name,
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "liked": liked,
                'comment_form': CommentForm(),
            },
        )

    def post(self, request, slug):
        """
        POST request for processing the CommentForm
        data passed from the reviews details page and if
        form is valid saves comment to database.
        """
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
    """
        Class based view to display edit comment
        page with comment form relative to the
        current selected review and utilising
        the built in django updateview for saving
        updated data to the database.
    """
    model = Comment
    template_name = 'reviews/edit_comment.html'
    fields = [
        'body',
        ]


class DeleteComment(DeleteView):
    """
        Class based view to delete the selected
        comment using the built in Django Deleteview.
    """
    model = Comment
    template_name = 'reviews/delete_comment.html'
    success_url = reverse_lazy('reviews')


class ReviewLike(View):
    """
        Class based view to toggle the liked status for
        the selected comment and saving to the database.
    """
    def post(self, request, slug):
        """
        POST request for processing the review liked status
        data passed from the reviews details page and if
        form is valid updates and saves status to database.
        """
        post = get_object_or_404(Review, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('review_details', args=[slug]))
