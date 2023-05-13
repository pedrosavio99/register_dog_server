from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cadastro
from .serializers import CadastroSerializer


@api_view(['POST'])
def cadastrar(request):
    serializer = CadastroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def listar(request):
    cadastros = Cadastro.objects.all()
    serializer = CadastroSerializer(cadastros, many=True)
    return Response(serializer.data)

