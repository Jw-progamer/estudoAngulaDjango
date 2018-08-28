from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Revista

class RevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revista
        fields = ('id','codigo','titulo','pagina','publicacao','qtde')