from rest_framework import serializers
from .models import Anuncio, Foto

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = ['id', 'imagem', 'ordem']
        read_only_fields = ['id', 'ordem'] #Campos que não podem ser alterados.

class AnuncioListSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.username", read_only=True)
    foto_principal = serializers.SerializerMethodField() #Criando campo para exibir apenas no anuncio

    class Meta:
        model = Anuncio
        fields = ['id', 'marca', 'modelo', 'ano', 'preco', 'foto_principal', 'owner']

    def get_foto_principal(self, obj): #metodo customizado para buscar a primeira foto ( foto principal )
        foto = obj.fotos.order_by('ordem').first() #pega a primeira foto relacionada a este anuncio
        if foto:
            return foto.imagem.url
        return None

class AnuncioDetailSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.username", read_only=True)
    fotos = FotoSerializer(many=True, read_only=True)

    class Meta:
        model = Anuncio
        fields = [
            'id', 'marca', 'modelo', 'ano',
            'km', 'preco', 'telefone_contato',
            'criado_em', 'fotos', 'owner'
        ]

class AnuncioCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = [
            'marca', 'modelo', 'ano',
            'km', 'preco', 'telefone_contato'
        ]
