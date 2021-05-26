from rest_framework.renderers import JSONRenderer
from datetime import datetime
import json
import json
import uuid
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
api_response = {}
orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

def home(request):
    print("We are here")
    apiKey = str(datetime.now())
    apiValue = str(uuid.uuid4())
    api_response[apiKey]=apiValue
    print(api_response)
    print(apiValue)
    sort_orders = dict(sorted(api_response.items(), key=lambda x: x[0], reverse=True))
    # return JsonResponse(json.JSONEncoder.default(api_response))
    # content = JSONRenderer().render(api_response)
    return JsonResponse(sort_orders, safe= False)
