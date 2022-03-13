

class CreateReview(View):

    def get(self, request, *args, **kwargs):        
        





class CreateReview(View):

    def get(self, request, slug, *args, **kwargs):
        form = CreateReviewForm()
        context = {'form': form }
        return render(request, 'create_review.html', context)


    def post(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = ReviewForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = review
            comment.save()
        else:
            comment_form = ReviewForm()

        return render(
            request,
            "reviews_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                'comment_form': ReviewForm(),
            },
        )



"/{0}/".format(
            self.slug 
        )