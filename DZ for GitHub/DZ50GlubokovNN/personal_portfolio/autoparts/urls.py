from django.urls import path
from .views import *

app_name = 'autoparts'

urlpatterns = [
    path('', PartsHome.as_view(), name='autoparts'),
    path('category/<slug:cat_slug>/', PartsCategory.as_view(), name='category'),
    path('part/<slug:part_slug>/', ShowPart.as_view(), name='part'),
]