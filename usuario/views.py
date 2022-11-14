from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
        #Verifica se a senha foi informada, caso contrário retornará um senha aleatório de 8 dígitos
        senha = Usuario.verificarSenha(request)

        #Verifica se a senha tem pelo menos 4 caracteres, caso não tenha será exibido uma mensagem pedindo pra informar uma senha do tamanho necessário
        if len(senha) < 4:
            return Response('Informe uma senha com pelo menos 4 caracteres')

        #Caso tenha pelo menos 4 caracteres o usuário será criado
        else:
            usuario = Usuario.objects.create(
                login = request.data['login'],
                senha = senha,
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