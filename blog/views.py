from django.shortcuts import render
from blog.models import Post


def home(request):
    # a list of dictionaries( named posts) assigned to a variable 'posts' inside another dictionary (named context)
    context={
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'Blog-about'})