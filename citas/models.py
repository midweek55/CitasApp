from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class Medico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=[('creada', 'Creada'), ('finalizada', 'Finalizada')])

    def __str__(self):
        return f"{self.cliente.usuario.username} - {self.medico.usuario.username} - {self.fecha_hora}"