from django.db import models
import uuid

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    login = models.CharField(max_length=200)
    senha = models.CharField(max_length=8)
    dataDeNascimento = models.DateField()

    def gerarSenhaAleatoria(usuario):
        senha = Usuario.objects.make_random_password(length=8)

    def __str__(self):
        return self.login