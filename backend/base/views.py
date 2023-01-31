from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


from .products import products

# Create your views here.

@api_view('GET', '')
def getRoutes(request):
    return JsonResponse('Hello', safe=False)


def getProducts(request):
    return JsonResponse(products, safe=False)
