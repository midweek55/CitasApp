from django.urls import path
from .views import ListaCitas, DetalleCita

urlpatterns = [
    path('citas/', ListaCitas.as_view(), name='lista-citas'),
    path('citas/<int:pk>/', DetalleCita.as_view(), name='detalle-cita'),
]