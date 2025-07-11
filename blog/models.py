from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='photo', blank=True, null=True, verbose_name='Фото')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    publication_sign =  models.BooleanField(default=True)
    views =  models.PositiveIntegerField(default=0, verbose_name="Количество просмотров",
                                         help_text="Количество раз, когда пост был просмотрен",)


    def __str__(self):
        return f'{self.title} {self.content}'


    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'


