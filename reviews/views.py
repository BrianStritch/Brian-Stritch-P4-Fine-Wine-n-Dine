from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.views import generic, View 
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView, UpdateView
from django.http import HttpResponseRedirect
from .models import Review, Comment
from .forms import CommentForm, CreateReviewForm, EditReviewForm


class ReviewsList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'reviews/reviews.html'
    paginate_by = 8


class ReviewsDetail(View):

    def get(self, request, slug, *args, **kwargs):
        form = EditReviewForm()
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
                'form': form,
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
        form = EditReviewForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = review
            comment.save()

        else:
            comment_form = CommentForm()
            form = EditReviewForm()

        return render(
            request,
            "reviews/reviews_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                'comment_form': CommentForm(),
                'form': form,
            },
        )



##############################################  comment editing form ########################################

class EditComment(UpdateView):
    model = Comment
    template_name = 'reviews/edit_comment.html'
    fields = [
        'body',
        ]








# class EditComment(TemplateView):
#     template_name = "reviews/edit_comment.html"

#     def get(self, request, slug, *args, **kwargs):
#         queryset = Review.objects.all()
#         review = get_object_or_404(queryset, id=id)
#         form = CommentForm()
#         id=id
        

#         return render(
#             request,
#             "reviews/edit_comment.html",
#             {
#                 'form': CommentForm(),
#                 'id':id
#             },
#         )   
#     def post(self, request, slug, *args, **kwargs):
        
#             queryset = Comments.objects.filter(id=request.comment.id)
#             review = get_object_or_404(queryset, slug=slug, id=id)
#             comment_form = CommentForm(data=request.POST)

#             if comment_form.is_valid():
#                 comment_form.instance.email = request.user.email
#                 comment_form.instance.name = request.user.username
#                 comment = comment_form.save(commit=False)
#                 comment.post = review
#                 comment.save()
#             else:
#                 comment_form = CommentForm()

#             return render(
#                 request,
#                 self.template_name ,
#                 {
#                     "review": review,
#                     "comments": comments,
#                     "commented": True,
#                     "liked": liked,
#                     'comment_form': CommentForm(),
#                 },
#             )

##################################################################################



# class EditComment(TemplateView):
#     """
#     Edit profile template with form which allows users to Edit their username,
#     first name, last name, email address and a password with a password
#     verifcation check.
#     """
#     template_name = "reviews/edit_comment.html"

#     def get(self, request):
#         form = EditCommentForm()
#         return render(
#             request,
#             self.template_name,
#             {
#                 'form': form,
#             })

#     def post(self, request):
#         if request.method == 'POST':
#             queryset = Comments.objects.all()
#             review = get_object_or_404(queryset, slug=slug)
#             comment_form = CommentForm(data=request.POST)
#             title = comment_form.cleaned_data['title']
#             comment = queryset.filter(title=title)
#             comment.





#             form = EditProfileForm(request.POST,)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect(reverse('profile'))

#         else:
#             form = EditProfileForm(instance=request.user)
#             details = {
#                 'form': form,
#             }
#             return render(request, self.template_name, details)
































########################################################################################





class ReviewLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Review, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('review_details', args=[slug]))


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




###############################################################################################

class EditReview(UpdateView):
    model = Review
    template_name = 'reviews/edit_review.html'
    fields = [
        'title',
        'content',
        'featured_image',
        'excerpt',
        ]



# class Edit_________________Review(TemplateView):
#     """
#     Edit profile template with form which allows users to Edit their username,
#     first name, last name, email address and a password with a password
#     verifcation check.
#     """
#     template_name = 'reviews/edit_review.html'

#     def get(self, request, slug):
#         form = EditReviewForm()
#         return render(
#             request,
#             self.template_name,
#             {
#                 'form': form,
#             })

#     def post(self, request, slug):
#         if request.method == 'POST':            
#             review = get_object_or_404(Review, id=slug)
#             form = EditReviewForm(request.POST, instance=request.user)
#             if form.is_valid():
#                 review.content = form.cleaned_data['content']
#                 review.featured_image = form.cleaned_data['featured_image']
#                 review.excerpt = form.cleaned_data['excerpt']
#                 form.save()
#                 return render(request, self.template_name, {'form':form})

#         else:
#             form = EditReviewForm(instance=request.user)
#             details = {
#                 'form': form,
#             }
#             return render(request, self.template_name, details)


































# class EditReview(TemplateView):
#     """
#     Edit profile template with form which allows users to Edit the reviews to which the user
#     has previously created.
#     """
#     template_name = 'reviews/edit_review.html'

#     def get(self, request, slug, *args, **kwargs):
#         form = EditReviewForm()
#         return render(
#             request,
#             self.template_name,
#             {
#                 'form': form,
#             })



#     # def post(self, request, slug):
#     #     if request.method == 'POST':

#     #         form = EditReviewForm(request.POST)
#     #         form.instance.author = request.user
#     #         if form.is_valid():
#     #             form.save()
#     #             return HttpResponseRedirect(reverse('review_details'))

#     #     else:
#     #         form = EditProfileForm(instance=request.user)
#     #         details = {
#     #             'form': form,
#     #         }
#     #         return render(request, self.template_name, details)

#     def post(self, request, slug, *args, **kwargs):
#         form = EditReviewForm(request.POST)
#         if request.method == 'POST':
#             queryset = Review.objects.filter(id=request.user.id)
#             filtered_review = queryset.filter(self.slug)         
#             review = get_object_or_404(Review, filtered_review)
#             #if review.filter(id=self.request.user.id).exists():
#             form = EditReviewForm(request.POST)
#             review.content = form.cleaned_data['content']
#             review.featured_image = form.cleaned_data['featured_image']
#             review.excerpt = form.cleaned_data['excerpt']
#             if form.is_valid():
#                 review = form.save(commit=False)
#                 form.post = review
#                 form.save()
#                 return HttpResponseRedirect(reverse('review_details', args=[slug]))

#         else:
#             form = EditReviewForm()
#             details = {
#                 'form': form,
#             }
#             return render(request, self.template_name, details)



# class EditReview(TemplateView):
#     """
#     Edit profile template with form which allows users to Edit their username,
#     first name, last name, email address and a password with a password
#     verifcation check.
#     """
#     template_name = 'reviews/edit_review.html'

#     def get(self, request, slug):
#         form = EditReviewForm()
#         return render(
#             request,
#             self.template_name,
#             {
#                 'form': form,
#             })

#     def post(self, request, slug):
#         if request.method == 'POST':
#             form = EditReviewForm(request.POST)
#             if form.is_valid():
#                 #title = request.title
#                 review = Review.objects.get(author=request.user, slug=slug)           
#                 review.content = form.cleaned_data['content']
#                 review.featured_image = form.cleaned_data['featured_image']
#                 review.excerpt = form.cleaned_data['excerpt']
#                 form.save()
#                 return HttpResponseRedirect(reverse('review_details'))

#         else:
#             form = EditProfileForm()
#             details = {
#                 'form': form,
#             }
#             return render(request, self.template_name, details)
























































