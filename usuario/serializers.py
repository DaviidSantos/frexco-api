from rest_framework.serializers import ModelSerializer
from .models import Usuario

def UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
