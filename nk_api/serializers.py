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