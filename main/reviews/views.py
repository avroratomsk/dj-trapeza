from django.http import HttpResponse
from django.shortcuts import render

from reviews.models import Reviews

def reviews(request):
  reviews = Reviews.objects.filter(status=True)
  
  context = {
    "reviews":reviews
  }
  return render(request, "pages/reviews/reviews.html", context)

def reviews_detail(requset, slug):
  return HttpResponse(f"{slug} - отзыв")
