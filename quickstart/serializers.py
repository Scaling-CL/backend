from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('id', 'nombres', 'apellidos', 'email',
                  'telefono', 'celular', 'direccion1',
                  'direccion2', 'comuna', 'region',
                  'pais', 'tipoFacturacion', 'rutEmpresa',
                  'nombreEmpresa')


class VeterinariaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Veterinaria
        fields = ('id', 'nombre', 'nombreVeterinario', 'email',
                  'telefono', 'celular', 'direccion1',
                  'direccion2', 'comuna', 'region', 'pais')


class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = ('cliente', 'id', 'nombre', 'fechaNacimiento',
                  'veterinarioAnterior', 'especie', 'raza',
                  'sexo', 'peso')