from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog

def blog_index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_index.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})

def create(request):
    if request.method == 'POST':
        Blog.objects.create(title=request.POST['title'], content=request.POST['content'])
        return redirect('blog_index')
    return render(request, 'blog/create.html')

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect('blog_index')
    return render(request, 'blog/update.html', {'blog': blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('blog_index')
