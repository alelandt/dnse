from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
from .gmaps import google_lookup
import googlemaps

google_maps = googlemaps.Client(key='AIzaSyBtrgoXtMw1l4TBaRfUFteqps4EoKGLBc')

def index(request):
    form = forms.SearchForm()
    return render(request, "index.html", {'form': form})

@csrf_exempt
def search_results(request):
    names = request.POST.get('search_q')
    longitude = request.POST.get('longitude')
    latitude = request.POST.get('latitude')
    new_names = google_lookup(longitude, latitude)
    return JsonResponse(latitude, safe=False)

