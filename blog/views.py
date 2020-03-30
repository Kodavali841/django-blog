from django.shortcuts import render

posts=[

    {
        'author':'CoreyMS',
        'title':'Blog post 1' ,
        'content':'First post content',
        'date_posted':'March 28,2020'
    },
    {
        'author':'Jane Doe',
        'title':'Blog post 2' ,
        'content':'Secpnd post content',
        'date_posted':'March 29,2020'
    }
]

def home(request):
    # a list of dictionaries( named posts) assigned to a variable 'posts' inside another dictionary (named context)
    context={
        'posts': posts,
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'Blog-about'})