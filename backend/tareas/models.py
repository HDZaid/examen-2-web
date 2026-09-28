from django.db import models


class Tarea(models.Model):

    class Estado(models.TextChoices):
        PENDIENTE = "pendiente", "Pendiente"
        COMPLETADA = "completada", "Completada"

    titulo = models.CharField(max_length=200)
    curso = models.CharField(max_length=150)
    fecha_entrega = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE
    )

    class Meta:
        ordering = ["fecha_entrega", "id"]

    def __str__(self):
        return self.titulo