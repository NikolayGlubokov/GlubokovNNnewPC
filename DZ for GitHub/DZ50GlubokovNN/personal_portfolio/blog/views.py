from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required

@login_required
def blogs(request):
    blog = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'blogs': blog})
@login_required
def detail(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html',{'blog': blog})
# Create your views here.
