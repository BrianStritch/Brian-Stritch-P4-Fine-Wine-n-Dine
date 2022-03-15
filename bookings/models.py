from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


BOOKING_STATUS = ((0, 'Pending'), (1, 'Approved'), (3, 'Completed'))

# Create your models here.

# Booking Model
class Booking(models.Model):
    booking_id = models.IntegerField()
    booking = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # noqa    
    dietary_notes = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    number_of_guests = models.IntegerField(range(10,1))
    number_of_tables = models.IntegerField()
    availability = models.BooleanField(default=True)
    #meal_time = 

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    



# Approval model
class Booking_approval(models.Model):

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='Approval')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# Reviews Model
# class Booking(models.Model):
#     post = models.CharField(max_length=200)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=200, unique=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # noqa
    #updated_on = models.DateTimeField(auto_now=True)
    # Dietary_notes = models.TextField()
    #featured_image = CloudinaryField('image', default='placeholder')
    # excerpt = models.TextField(blank=True)
    # created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    # likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    # class Meta:
    #     ordering = ['-created_on']

    # def __str__(self):
    #     return self.title

    # def number_of_likes(self):
        # return self.likes.count()
