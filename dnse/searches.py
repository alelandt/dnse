from django.http import HttpResponse, HttpRequest
import requests
import numpy as np

def name_parse(names):
    temp =[]
    url='https://sugapi.verisign-grs.com/ns-api/2.0/segment?name=' + names

    header={'X-NAMESUGGESTION:676226de70489ae087ba1cd63cf9345a'}

    r=requests.get(url, headers=headers)
   results=r.text
   for entries in results: 
	for items in entries.get('segmentedName'):
		temp.append()   
   # 676226de70489ae087ba1cd63cf9345a # api key
    return np.unique(temp) 

def verisign_lookup(names):
    return "junk"

