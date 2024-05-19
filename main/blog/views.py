from django.shortcuts import render

from blog.models import BlogSettings, Post

def blog(request):
  articles = Post.objects.filter(status=True)
  try:
    blog_set = BlogSettings.objects.get()
  except:
    blog_set = BlogSettings()
  context = {
    "articles": articles,
    "blog_setings": blog_set
  }
  return render(request, "pages/blog/blog.html", context)

def blog_detail(request, slug):
  pass

def post(request, slug):
  article = Post.objects.get(slug=slug) 
  articles = Post.objects.filter(status=True).exclude(slug=slug)
  
  context = {
    "article": article,
    "articles": articles,
  }
  
  return render(request, "pages/blog/blog_detail.html", context)