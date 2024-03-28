from django.shortcuts import render

from blog.models import Blog

def blog(request):
  return render(request, "pages/blog/blog.html")

def blog_detail(request, slug):
  article = Blog.objects.filter(status=True) 
  
  context = {
    "article": article
  }
  return render(request, "pages/blog/blog_detail.html", article)