from django.shortcuts import render

# Create your views here.
def blog_home(request):
    """ A view to return the 'blog_home' page """

    return render(request, 'blog/index.html')
