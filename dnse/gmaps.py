from django.http import HttpResponse, HttpRequest
import json
import googlemaps
import numpy as np

google_maps = googlemaps.Client(key='AIzaSyBs072jMQc_jZQF8ePeyVrhGk0HGyKFMXA')

def google_lookup(lon, lat):
    temp = []
    results = google_maps.reverse_geocode((lat,lon))
    #print(results)
    for entries in results:
        for items in entries.get('address_components'):
            if str.isdigit(items.get('long_name')) != True and items.get('long_name') != 'United States':
                temp.append(items.get('short_name'))
            if str.isdigit(items.get('short_name')) != True and items.get('short_name') != 'United States':
                temp.append(items.get('short_name'))
    #print(np.unique(temp))
    return np.unique(temp)
