from django.http.response import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from places.models import Place


def get_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_serialized = {
        "title": place.title,
        "imgs": [image.file.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": str(place.lon),
            "lat": str(place.lat)
        }
    }
    return JsonResponse(place_serialized,
                        safe=False,
                        json_dumps_params={'ensure_ascii': False})


def index(request):
    places = []
    for place in Place.objects.all():
        places.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f'places/{place.id}/'
            }
        })

    places_geojson = {
        "type": "FeatureCollection",
        "features": places
    }
    context = {'places': places_geojson}
    return render(request, 'index.html', context)
