from django.contrib import admin
from .models import Exercise, Plan, Photo, Comment
# Register your models here.

admin.site.register(Exercise)
admin.site.register(Plan)
admin.site.register(Photo)
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)