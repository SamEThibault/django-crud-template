from django.shortcuts import render
from .models import Post


# Can pass query data to template using jinja2-like syntax
def home(request):

    context = {
        'title': 'Home',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})