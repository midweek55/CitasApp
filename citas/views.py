from rest_framework import generics
from .models import Cita
from .serializers import CitaSerializer

class ListaCitas(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class DetalleCita(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer