from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max

class Anuncio(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anuncios')
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    ano = models.PositiveIntegerField()
    km = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    telefone_contato = models.CharField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"


class Foto(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='fotos/')
    ordem = models.PositiveIntegerField(editable=False, null=True, blank=True)

    class Meta:
        ordering = ['ordem']

    def save(self, *args, **kwargs):
        if self.ordem is None:
            ultima_ordem = self.anuncio.fotos.aggregate(Max('ordem'))['ordem__max'] or 0
            self.ordem = ultima_ordem + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Foto {self.ordem} do Anuncio {self.anuncio.id}"
