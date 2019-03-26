from django.shortcuts import render


posts = [
{
    'author': 'Denzel97',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'August 27, 2018'
},
{
    'author': 'Denzel',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'August 28, 2018'
}
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'mtaa/home.html', context)


def about(request):
    return render(request, 'mtaa/about.html', {'title': 'About'})