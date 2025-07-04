from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание продукта')
    image = models.ImageField(upload_to='name/photo', blank=True, null=True, verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, verbose_name='категория',
                                 null=True, blank=True, related_name='products')
    price = models.IntegerField(verbose_name='цена за покупку', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения', auto_now=True)


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['category']


    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание категории')


    class Meta:
        verbose_name = "Наименование категории"
        verbose_name_plural = "Категории"


    def __str__(self):
        return f"{self.name}"
