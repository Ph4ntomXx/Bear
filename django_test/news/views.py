from django.shortcuts import render
from .models import News

def news_home(request):
    news = News.objects.order_by('-published_date')
    return render(request, 'news/news_home.html', {'news': news})