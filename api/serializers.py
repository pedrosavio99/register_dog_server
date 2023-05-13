from rest_framework import serializers

from .models import Cadastro


class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ['id', 'nome', 'matricula']
