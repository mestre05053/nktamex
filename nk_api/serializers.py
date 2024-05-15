from rest_framework import serializers
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


    '''
    class ToySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    release_date = serializers.DateTimeField()
    toy_category = serializers.CharField(max_length=200)
    was_included_in_home = serializers.BooleanField(required=False)
    
    def create(self, validated_data):
    return Toy.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description',
    instance.description)
    instance.release_date = validated_data.get('release_date',
    instance.release_date)
    instance.toy_category = validated_data.get('toy_category',
    instance.toy_category)
    instance.was_included_in_home =
    validated_data.get('was_included_in_home', instance.was_included_in_home)
    instance.save()
    return instance
    
    '''