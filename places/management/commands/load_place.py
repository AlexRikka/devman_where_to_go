from django.core.management.base import BaseCommand
from django.core.files import File
from places.models import Place
import requests
import json
import os


class Command(BaseCommand):
    help = 'Загружает в базу данные о локации в формате json.'

    def add_arguments(self, parser):
        parser.add_argument('place_json', nargs=1, type=str)

    def handle(self, *args, **options):
        response = requests.get(url=options['place_json'][0])
        response.raise_for_status()
        place_raw = json.loads(response.content)
        place, created = Place.objects\
            .update_or_create(title=place_raw['title'],
                              short_description=place_raw['description_short'],
                              long_description=place_raw['description_long'],
                              lat=place_raw['coordinates']['lat'],
                              lon=place_raw['coordinates']['lng'])

        if created:
            for i, image_url in enumerate(place_raw['imgs'],  start=1):
                response = requests.get(url=image_url)
                response.raise_for_status()
                image_path = os.path.join('media', os.path.basename(image_url))

                with open(image_path, 'wb') as f:
                    f.write(response.content)
                with open(image_path, 'rb') as f:
                    place.images.create(number=i,
                                        file=File(f),
                                        place=place)
            self.stdout.write(self.style.SUCCESS(
                f'Успешно загружена локация #{place.id}'))
        else:
            self.stdout.write(self.style.SUCCESS(
                'Такая локация уже есть в базе'))
