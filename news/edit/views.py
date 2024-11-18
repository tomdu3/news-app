from django.shortcuts import render
from .models import News

# Create your views here.
def home(request):
    # add news from database
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'edit/home.html', context)
