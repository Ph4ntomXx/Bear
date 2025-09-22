from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField('Название', max_length=50)
    content = models.TextField('Контент')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.pk)])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'