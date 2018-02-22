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
    locationData = False
    names = request.POST.get('search_q')
    return JsonResponse(request.POST.get('search_q'), safe=False)

