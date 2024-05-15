from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Api, Art

class APiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ('fechaemision','nombre','apellidos','email','telefono','direccion','ciudad','estado','codigopostal')

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = ('articulo','rama','descripcion1','nombrecorto','grupo','categoria',)

class UserDataSerializer(serializers.ModelSerializer):
    #pk = serializers.IntegerField(read_only=True)
    #fechaemision = serializers.DateTimeField()
    nombre = serializers.CharField(max_length=150)
    apellidos = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=150)

    class Meta:
        model = Api
        managed = True
        verbose_name = 'Api'
        verbose_name_plural = 'Apis'
        fields = ('pk','nombre','apellidos','email')
    
    def create(self, validated_data):
        return Api.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.fechaemision = validated_data.get('fechaemision', instance.fechaemision)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    user_data = serializers.PrimaryKeyRelatedField(many=True, queryset=Api.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'user_data']