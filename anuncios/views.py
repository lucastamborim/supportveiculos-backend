from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Anuncio, Foto
from .serializers import (
    AnuncioListSerializer,
    AnuncioDetailSerializer,
    AnuncioCreateUpdateSerializer,
    FotoSerializer
)

from .permissions import IsOwnerOrReadOnly

class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all().order_by('-criado_em')
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return AnuncioListSerializer
        if self.action == "retrieve":
            return AnuncioDetailSerializer
        return AnuncioCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]
        return super().get_permissions()

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def adicionar_foto(self, request, pk=None):
        anuncio = self.get_object()

        if anuncio.owner != request.user:
            return Response({"detail": "Você não é o dono deste anúncio."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = FotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(anuncio=anuncio)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def listar_fotos(self, request, pk=None):
        anuncio = self.get_object()
        fotos = anuncio.fotos.order_by("ordem")
        serializer = FotoSerializer(fotos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'], url_path="deletar-foto/(?P<foto_id>[^/.]+)")
    def deletar_foto(self, request, pk=None, foto_id=None):
        anuncio = self.get_object()

        foto = get_object_or_404(Foto, id=foto_id, anuncio=anuncio)

        if anuncio.owner != request.user:
            return Response({"detail": "Você não é o dono deste anúncio."},
                            status=status.HTTP_403_FORBIDDEN)

        foto.imagem.delete(save=False)
        foto.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
