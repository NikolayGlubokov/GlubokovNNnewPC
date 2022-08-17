from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *
from django import forms

class PartsAdminForm(forms.ModelForm):
    content=forms.CharField(widget=CKEditorUploadingWidget())


    class Meta:
        model = Parts
        fields = '__all__'


class PartsAdmin(admin.ModelAdmin):
    form=PartsAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'content', 'price')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')

admin.site.register(Parts,PartsAdmin)
admin.site.register(Category, CategoryAdmin)
