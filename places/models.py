from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название')
    short_description = models.CharField(max_length=255,
                                         verbose_name='Краткое описание')
    long_description = models.TextField(null=True,
                                        blank=True,
                                        verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    file = models.ImageField(verbose_name='Файл',
                             upload_to='media')
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              related_name='images',
                              verbose_name='Локация')

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.number} {self.place.title}"
