from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Anuncio, Foto
from .serializers import (AnuncioListSerializer,AnuncioDetailSerializer,AnuncioCreateUpdateSerializer,FotoSerializer)
from .permissions import IsOwnerOrReadOnly

class AnuncioListView(generics.ListAPIView):
    queryset = Anuncio.objects.order_by('-criado_em')
    serializer_class = AnuncioListSerializer

class AnuncioCreateView(generics.CreateAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioCreateUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AnuncioDetailView(generics.RetrieveAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioDetailSerializer

class AnuncioUpdateView(generics.UpdateAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['patch', 'put']

class AnuncioDeleteView(generics.DestroyAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

class FotoUploadView(generics.CreateAPIView):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, anuncio_id):
        anuncio = get_object_or_404(Anuncio, id=anuncio_id)

        if anuncio.owner != request.user:
            return Response(
                {"detail": "Você não é o dono deste anúncio."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = FotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(anuncio=anuncio)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FotoDeleteView(generics.DestroyAPIView):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_destroy(self, instance):
        instance.imagem.delete(save=False)
        super().perform_destroy(instance)


class FotoListView(generics.ListAPIView):
    serializer_class = FotoSerializer

    def get_queryset(self):
        anuncio_id = self.kwargs.get("anuncio_id")
        return Foto.objects.filter(anuncio_id=anuncio_id).order_by("ordem")
