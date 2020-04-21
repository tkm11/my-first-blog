from django.shortcuts import render

def post_lite(request):
    return render(request, 'blog/post_lite.html', {})
