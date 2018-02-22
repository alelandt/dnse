from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms

def index(request):
    form = forms.SearchForm()
    return render(request, "index.html", {'form': form})

@csrf_exempt
def search_results(request):
    return JsonResponse(request.POST.get('search_q'), safe=False)
