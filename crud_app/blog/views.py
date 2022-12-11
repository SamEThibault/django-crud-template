from django.shortcuts import render

# test data before integrating db
posts = [
    {
        'author': 'Sam',
        'title': 'blog post 1',
        'content': 'hello there',
        'date_posted': 'Dec 11, 2022'
    },
    {
        'author': 'Sam again',
        'title': 'blog post 2',
        'content': 'hello there, again',
        'date_posted': 'Dec 12, 2022'
    }
]


# Can pass data to template using context var, for example
def home(request):

    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})