from django.db import models

class News(models.Model):
    title = models.CharField('Название', max_length=50)
    content = models.TextField('Контент')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'