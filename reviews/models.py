from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.shortcuts import render, reverse
from django.template.defaultfilters import slugify

STATUS = ((0, 'Draft'), (1, 'Published'))


# Reviews Model
class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_posts') # noqa , default=1  
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='review_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
        return reverse('reviews')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()



# comments model
class Comment(models.Model):

    post = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']    

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
    
    def get_absolute_url(self):
        return reverse('reviews')


    


