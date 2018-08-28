from django.db import models

# Create your models here.
class Revista(models.Model):
    codigo = models.CharField(max_length = 25, unique=True)
    titulo = models.TextField(max_length = 100)
    pagina = models.IntegerField()
    publicacao = models.DateField()
    qtde = models.IntegerField()

    def __str__(self):
        return self.titulo
    