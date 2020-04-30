from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=120)
    body = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published']


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='Новость', related_name='comments')
    author = models.CharField(max_length=200, verbose_name='Автор')
    body = models.CharField(max_length=120, verbose_name='Комментарий')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-published',)