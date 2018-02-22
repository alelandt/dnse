from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, "index.html")

def search_results(request):
    return JsonResponse("empty")
