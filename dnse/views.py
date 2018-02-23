from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
from .gmaps import google_lookup
from .dict import dict_lookup
import googlemaps
from wordsegment import load, segment
from .blob import strip_out, combine_all, strip_space, check_data, exact_check
from .valid import check_url
import json
from difflib import SequenceMatcher

# lol this is a mess
tlds = ['boats', 'yachts', 'homes', 'autos', 'motorcycles', 'com', 'org', 'net']
def index(request):
    form = forms.SearchForm()
    return render(request, "index.html", {'form': form})

@csrf_exempt
def search_results(request):
    names = request.POST.get('search_q')
    if check_url(names):
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        location_names = google_lookup(longitude, latitude)
        locations = list(map(strip_out, location_names))
        load()
        wlist = segment(names.split('.')[0])
        synlist = dict_lookup(wlist)
        retlist = combine_all(locations, synlist, tlds)
        returnlist = []
        temp = names.split('.')[0]
        for entries in retlist:
            if SequenceMatcher(None,temp,entries).ratio() >= 0.5:
                returnlist.append(entries)
        returnlist = list(set(returnlist))
        mylist = sorted(returnlist, key=lambda x: temp,reverse=False)
        mylist = list(map(strip_space, mylist)) 
        finalval = check_data(mylist)
        return JsonResponse({"retlist": finalval}, safe=False)
    else:
        return JsonResponse("", safe=False)

