from rest_framework import generics
from .models import Anuncio
from .serializers import AnuncioListSerializer, AnuncioDetailSerializer, AnuncioCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
