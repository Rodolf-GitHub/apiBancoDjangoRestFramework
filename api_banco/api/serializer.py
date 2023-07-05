from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields='__all__'
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields='__all__'
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empresa
        fields='__all__'
class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model=Solicitud
        fields='__all__'