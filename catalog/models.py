from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание продукта')
    image = models.ImageField(upload_to='name/photo', blank=True, null=True, verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, verbose_name='категория',
                                 null=True, blank=True, related_name='products')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения')


    class Meta:
        verbose_name = "Наименование"
        verbose_name_plural = "Категории"
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

"""В приложении каталога создайте модели Product и Category и опишите для них базовые настройки.
Описание моделей:
    Product :
        наименование,
        описание, description
        изображение, image
        категория,  category
        цена за покупку,  purchase price
        Дата создания,  created_at
        Дата последнего изменения.  updated_at
        
    Category :
        наименование,
        описание.
        
Модель продукта связана с моделью категории через ForeignKey

    Поля «Дата создания» и «Дата последнего изменения» стали стандартом для моделей. Их общепринятые названия —
    created_at  и updated_at соответственно.
"""