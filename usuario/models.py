from django.db import models
import uuid
import random
import string

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    login = models.CharField(max_length=200, unique=True)
    senha = models.CharField(max_length=8, null=True, blank=True)
    dataDeNascimento = models.DateField()

    def verificarSenha(request):
        if not request.data['senha']:
            senha = Usuario.gerarSenha()
        elif request.data['senha']:
            senha = request.data['senha']

        return senha

    def gerarSenha():
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))

    def atualizarDados(usuario, request):
        if request.data['login']:
            usuario.login = request.data['login']
        
        if request.data['senha']:
            usuario.login = request.data['senha']

        return usuario

    def __str__(self):
        return self.login