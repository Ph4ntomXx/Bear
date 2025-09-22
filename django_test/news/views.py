from django.shortcuts import render
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = News.objects.order_by('-published_date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/create.html'

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = '/news/'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'news/create.html', {
                'form': NewsForm(),
                'success': True
            })
    else:
        form = NewsForm()

    return render(request, 'news/create.html', {'form': form})
