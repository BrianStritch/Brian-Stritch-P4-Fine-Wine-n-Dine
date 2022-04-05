"""
    imports  -----------------reviews models.py----------------------
"""
# third party imports
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import reverse

from cloudinary.models import CloudinaryField

STATUS = (
    (0, 'Draft'),
    (1, 'Published')
    )


class Review(models.Model):
    """
        Class based model for Reviews
    """
    title = models.CharField(max_length=200, unique=True)

    slug = models.SlugField(max_length=200, unique=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='review_posts'
        )

    updated_on = models.DateTimeField(auto_now=True)

    content = models.TextField()

    featured_image = CloudinaryField(
        'image',
        default='placeholder'
        )

    excerpt = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    status = models.IntegerField(choices=STATUS, default=0)

    likes = models.ManyToManyField(
        User,
        related_name='review_likes',
        blank=True
        )

    class Meta:
        """
            meta class to set the order in which
            the reviews are displayed
        """
        ordering = ['-created_on']

    def get_absolute_url(self):
        """
            function to define the reverse URL
            for after a review is created or edited
        """
        return reverse('reviews')

    def save(self, *args, **kwargs):
        """
            function to edit and save the slug
            for after a review is created or edited
        """
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """
            function to return the review title as a string
        """
        return str(self.title)

    def number_of_likes(self):
        """
            function to return the number of likes on a review
        """
        return self.likes.count()


class Comment(models.Model):
    """
        Class based model for Comments
    """

    post = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
        )

    name = models.CharField(max_length=80)

    email = models.EmailField()

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)

    class Meta:
        """
            meta class to set the order in which
            the reviews are displayed
        """
        ordering = ['created_on']

    def __str__(self):
        """
            function to return the commentbody and the author as a string
        """
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """
            function to define the reverse URL
            for after a comment is created or edited
        """
        return reverse('reviews')
