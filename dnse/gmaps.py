from django.http import HttpResponse, HttpRequest

import googlemaps

def google_lookup(locationData):
    temp = []
    address = maps.geolocate()
    results = google_maps.search(location=address)
    for entries in results:
        if entries.shortname.contains(' ') == False:
            temp.append(entries.short_name)
    return temp
