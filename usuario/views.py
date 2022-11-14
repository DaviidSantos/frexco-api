from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer

@api_view(['GET'])
def usuario_list(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

def usuario_detail(request, login):
    data = login
    return JsonResponse(data, safe=False)