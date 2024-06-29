from audioop import reverse

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import viewsets
from rest_framework.views import APIView
from django.views import generic

from django.shortcuts import render


from app.models.CorpoModel import Corpo
from app.serializer.sCorpo import CorpoSerializer


class CorpoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Corpo.objects.all()
    serializer_class = CorpoSerializer

    def get_queryset(self):
        usuario = self.request.user
        if usuario.groups.filter(name="Pesquisadores"):
            return Corpo.objects.all()
        elif usuario.groups.filter(name="Administradores"):
            return Corpo.objects.all()
