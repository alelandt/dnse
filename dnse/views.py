from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
from .gmaps import google_lookup
from .dict import dict_lookup
import googlemaps
from wordsegment import load, segment
from .blob import strip_out
from .valid import check_url

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
        newlist= synlist + locations
        return JsonResponse(",".join(newlist), safe=False)
    else:
        return JsonResponse("", safe=False)

