from django.contrib import admin
from .models import *


class PartsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'content', 'price')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')

admin.site.register(Parts,PartsAdmin)
admin.site.register(Category, CategoryAdmin)
