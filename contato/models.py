from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class ContatoDj(models.Model):
    nome = models.CharField(max_length=255)
    sobreNome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.CharField(max_length=255, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    exibir = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
