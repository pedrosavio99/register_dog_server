from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
