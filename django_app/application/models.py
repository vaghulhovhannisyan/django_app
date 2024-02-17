from django.db import models

class menu(models.Model):
    title = models.CharField('Название', max_length=50, blank=True)
    comment = models.TextField('Описания', blank=True)
    url = models.URLField('URL', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
