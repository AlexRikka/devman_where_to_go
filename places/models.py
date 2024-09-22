from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=255,
                             unique=True,
                             verbose_name='Название')
    short_description = models.TextField(blank=True,
                                         default='',
                                         verbose_name='Краткое описание')
    long_description = tinymce_models.HTMLField(blank=True,
                                                default='',
                                                verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    number = models.IntegerField(blank=True,
                                 default=0,
                                 verbose_name='Номер')
    file = models.ImageField(blank=True,
                             null=True,
                             verbose_name='Файл',
                             upload_to='media')
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              related_name='images',
                              verbose_name='Локация')

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.number} {self.place.title}"
