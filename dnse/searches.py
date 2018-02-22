from django.http import HttpResponse, HttpRequest
import requests

def name_parse(names):
    url = 'https://sugapi.verisign-grs.com/ns-api/2.0/segment'

    header = {APIKEY:'676226de70489ae087ba1cd63cf9345a', name:'runningmanbow',lang:eng,callback:'name_parse'}

    r = requests.get(url, headers=headers)
    r.json()
    print.r
   # 676226de70489ae087ba1cd63cf9345a # api key
    return r

def verisign_lookup(names):
    return "junk"

