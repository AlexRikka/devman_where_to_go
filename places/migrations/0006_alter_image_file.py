# Generated by Django 4.2.10 on 2024-10-06 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(default='', upload_to='media', verbose_name='Файл'),
        ),
    ]
