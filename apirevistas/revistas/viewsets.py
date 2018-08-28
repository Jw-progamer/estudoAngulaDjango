from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import Revista
from .serializers import RevistaSerializer

class RevistaViewSet(viewsets.ModelViewSet):
    queryset = Revista.objects.all()
    serializer_class = RevistaSerializer