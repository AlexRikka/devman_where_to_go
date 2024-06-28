from django.shortcuts import render
from places.models import Place


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
                "detailsUrl": "./static/places/moscow_legends.json"
            }
        })

    places_geojson = {
        "type": "FeatureCollection",
        "features": places
    }
    context = {'places': places_geojson}
    return render(request, 'index.html', context)
