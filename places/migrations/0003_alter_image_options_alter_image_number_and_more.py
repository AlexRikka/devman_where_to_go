# Generated by Django 4.2.10 on 2024-08-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['number']},
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.IntegerField(blank=True, default=0, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=models.TextField(blank=True, default='', verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, default='', verbose_name='Краткое описание'),
        ),
    ]
