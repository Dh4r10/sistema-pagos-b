from rest_framework import serializers
from .models import *
from .models import AuthUser # Asegúrate de importar tu modelo personalizado
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # get perfil
        # Obtén el perfil asociado al usuario
        tipo_usuario = user.tipo_usuario

        # Si el perfil existe, obtén su idperfil
        if tipo_usuario:
            token['id'] = tipo_usuario.id
        else:
            # Si no hay perfil asociado, puedes manejarlo como desees
            token['id'] = None
        # ...

        return token

# this serializer is already with url

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('__all__')

    def create(self, validated_data):
        # Extraemos el valor del ID del perfil
        user = AuthUser(**validated_data)
        validated_data['password'] = make_password(
            validated_data.get('password'))
        id = validated_data.get('id')

        return super().create(validated_data)