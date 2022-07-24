from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id','title','cat','time_completed','photo','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_completed')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
