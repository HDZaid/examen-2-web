from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Tarea
from .serializers import TareaSerializer


class TareaViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def get_queryset(self):
        queryset = Tarea.objects.all()

        estado = self.request.query_params.get("estado")

        if estado:
            estados_validos = [
                Tarea.Estado.PENDIENTE,
                Tarea.Estado.COMPLETADA,
            ]

            if estado not in estados_validos:
                raise ValidationError({
                    "estado": (
                        "El estado debe ser 'pendiente' "
                        "o 'completada'."
                    )
                })

            queryset = queryset.filter(estado=estado)

        return queryset

    @action(
        detail=True,
        methods=["patch"],
        url_path="completar"
    )
    def completar(self, request, pk=None):
        tarea = self.get_object()

        tarea.estado = Tarea.Estado.COMPLETADA

        tarea.save(
            update_fields=["estado"]
        )

        serializer = self.get_serializer(tarea)

        return Response(serializer.data)