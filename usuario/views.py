from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from .models import Usuario
from .serializers import UsuarioSerializer

@api_view(['GET', 'POST'])
def usuario_list(request):
    #Controla o Método GET
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        usuarios = Usuario.objects.filter(login__icontains = query)
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    #Controla o Método POST
    if request.method == 'POST':
        usuario = Usuario.objects.create(
            login = request.data['login'],
            senha = Usuario.verificarSenha(request),
            dataDeNascimento = request.data['dataDeNascimento']
        )

        serializer = UsuarioSerializer(usuario, many=False)
        return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, login):
    usuario = Usuario.objects.get(login=login)
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
         usuario = Usuario.atualizarDados(usuario, request)
         usuario.save()
         serializer = UsuarioSerializer(usuario, many=False)
         return Response(serializer.data)
        
    if request.method == 'DELETE':
        usuario.delete()
        return Response('Usuário Deletado com Sucesso')