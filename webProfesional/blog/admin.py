from django.contrib import admin
from .models import *

# Register your models here.




@admin.register(Post)
class BlogProject(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status',)
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

    class Media:
        css = {
            'all': ('core/assets/css/custom_ckeditor.css',)
        }

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')
    prepopulated_fields = {'slug': ('name',)}