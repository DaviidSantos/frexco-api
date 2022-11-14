from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer

@api_view(['GET'])
def usuario_list(request):
    query = request.GET.get('query')

    if query == None:
        query = ''

    usuarios = Usuario.objects.filter(login__icontains = query)
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def usuario_detail(request, login):
    usuario = Usuario.objects.get(login=login)
    serializer = UsuarioSerializer(usuario, many=False)
    return Response(serializer.data)