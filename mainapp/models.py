from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='название'),
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('-id',)