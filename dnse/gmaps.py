from django.http import HttpResponse, HttpRequest
import json
import googlemaps

google_maps = googlemaps.Client(key='AIzaSyBs072jMQc_jZQF8ePeyVrhGk0HGyKFMXA')

def google_lookup(lon, lat):
    temp = {}
    results = google_maps.reverse_geocode((lat,lon))
    print(results)
    for entries in results:
        print(entries)
        #if entries.shortname.contains(' ') == False:
        #    temp.append(entries.short_name)
    return temp
