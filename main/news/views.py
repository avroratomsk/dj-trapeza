from django.shortcuts import render
from django.shortcuts import render
from news.models import News, NewsSettings

def news(request):
  news = News.objects.filter(status=True) 
  try:
    new = NewsSettings.objects.get()
  except:
    new = NewsSettings()
  
  context = {
    "news": news,
    "new": new
  }
  return render(request, "pages/news/news.html", context)


def news_detail(request, slug):
  new = News.objects.get(slug=slug)
  news = News.objects.filter(status=True).exclude(slug=slug)
  context = {
    "new": new,
    "news": news
  }
  return render(request, "pages/news/news_detail.html", context)