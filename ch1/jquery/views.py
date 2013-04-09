import json

from django.http import HttpResponse
from django.shortcuts import render

def home(request):    
    return render(request, "home.html")

def show_params(request):    
    data = {
        "param1": request.GET['param1'],
        "param2": request.GET['param2'],
    }
    d= "param1"+request.GET['param1']+"  param2"+request.GET['param2']
    return HttpResponse(d)#json.dumps(data), mimetype="application/json")  