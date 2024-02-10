from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': "Столовая трапеза",
        'content': "Контент главной страницы"
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return HttpResponse('About page')
