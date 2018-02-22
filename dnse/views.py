from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
import googlemaps

google_maps = googlemaps.Client(key='AIzaSyBtrgoXtMw1l4TBaRfUFteqps4EoKGLBc')

def index(request):
    form = forms.SearchForm()
    return render(request, "index.html", {'form': form})

@csrf_exempt
def search_results(request):
    return JsonResponse(request.POST.get('search_q'), safe=False)

def google_lookup(request):
    temp = []
    address = maps.geolocate()
    results = google_maps.search(location=address)
    for entries in results:
        if entries.shortname.contains(' ') == False:
            temp.append(entries.short_name)
    return temp
