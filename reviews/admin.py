from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug','status', 'created_on')
    list_filter = ('status','created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('approved','created_on')
    list_display = ('name','body', 'post', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


