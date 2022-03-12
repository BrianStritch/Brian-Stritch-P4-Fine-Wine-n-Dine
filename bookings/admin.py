from django.contrib import admin
from .models import Booking, Booking_approval
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

#@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug','status', 'created_on')
    list_filter = ('status','created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


#@admin.register(Booking_approval)
class Booking_approval_Admin(admin.ModelAdmin):

    list_filter = ('approved','created_on')
    list_display = ('name','body', 'post', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)