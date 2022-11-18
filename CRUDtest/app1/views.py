from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def firstRequest(request):
    
    dataLst = []
    counter = 0
    x = requests.get('https://gorest.co.in/public/v2/users').json()
    
    for i in x: 
        dataLst.append(i)
         
    for i in dataLst:
        
        if(i['status'] == 'inactive'):
            counter+=1
        print(i['status'])  
            
    print(counter)
    
    # return counter
        
    return HttpResponse("hello world")
