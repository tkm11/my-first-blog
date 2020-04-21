from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_lite(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_lite.html', {'posts': posts})

