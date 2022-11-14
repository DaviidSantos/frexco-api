from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def usuario_list(request):
    data = [{
        'login': 'odavidsantos',
        'senha': 'd#663848',
        'dataDeNascimento': '18/06/2001'
        },
        {
        'login': 'dwvidpriv',
        'senha': 'd#663848',
        'dataDeNascimento': '18/06/2001'
        }
    ]
    return JsonResponse(data, safe=False)

def usuario_detail(request, login):
    data = login
    return JsonResponse(data, safe=False)