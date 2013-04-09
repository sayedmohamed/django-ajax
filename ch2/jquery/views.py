import json

from django.http import HttpResponse
from django.shortcuts import render

def ch1(request):
	return render(request, "home.html")

def show_params(request):
	d= "param1"+request.GET['param1']+"  param2"+request.GET['param2']
	return HttpResponse(d)


def ch2(request):
	return render(request, "ch2.html")

def nums(request):
	#data = {
    #    "param1": request.GET['param1'],
    #    "param2": request.GET['param2'],
    #}    
    n={ 
    	"fg": "red",
    	"bg": "black",
    	"fontSize":30,
    	"numbers": [1, 2, 3]
    }
    
    return HttpResponse(json.dumps(n), mimetype="application/json")    
