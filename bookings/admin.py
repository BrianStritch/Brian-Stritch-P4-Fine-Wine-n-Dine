from django.contrib import admin
from .models import Booking  #  ,  Booking_approval
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    # prepopulated_fields = {'slug': ('booking.id',)}
    list_display = ('primary_guest', 'availability','booking_status', 'booking_created_on')
    list_filter = ('booking_status','booking_created_on')
    search_fields = ['primary_guest', 'slug']
    summernote_fields = ('dietary_notes', 'additional_comments')


# #@admin.register(Booking_approval)
# class Booking_approval_Admin(admin.ModelAdmin):

#     list_filter = ('approved','created_on')
#     list_display = ('name','body', 'post', 'created_on', 'approved')
#     search_fields = ['name', 'email', 'body']
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(approved=True)