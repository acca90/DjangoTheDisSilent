from django.db import models


class Contatos(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
