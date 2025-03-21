from django.db import models
from django.utils import timezone

LISTA_CATEGORIAS = (
    ('ANALISES', 'Análises'),
    ('PROGRAMACAO', 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS', 'Outros'),
)

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes') # tem que passar um parâmaetro onde será armazenado as imagens
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now) # sem parenteses: quero preencher o horário e data atual / com parenteses: sempre que abrir esse filme seria rodado a função

    def __str__(self):
        return self.titulo


