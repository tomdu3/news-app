from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

# Create your views here.
def home(request):
    # add news from database
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'edit/home.html', context)


def add_news(request):
    '''
    add news to database
    '''
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
        return render(request, 'edit/add_news.html', {'form': form})
