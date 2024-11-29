from rest_framework import serializers
from .models import Divorcio, AsesoriaLegal

class DivorciosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Divorcio
        fields = '__all__'

class AsesoriasLegalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = AsesoriaLegal
        fields = '__all__'


