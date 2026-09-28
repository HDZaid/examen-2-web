from rest_framework import serializers
from .models import Tarea


class TareaSerializer(serializers.ModelSerializer):

    fechaEntrega = serializers.DateField(
        source="fecha_entrega"
    )

    class Meta:
        model = Tarea
        fields = [
            "id",
            "titulo",
            "curso",
            "fechaEntrega",
            "estado",
        ]