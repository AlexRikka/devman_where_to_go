# Generated by Django 4.2.10 on 2024-09-22 20:24

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_options_alter_image_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
    ]