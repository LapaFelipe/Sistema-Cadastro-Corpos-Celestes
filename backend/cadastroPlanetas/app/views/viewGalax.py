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

from app.models.GalaxiaModel import Galaxia
from app.serializer.sGalax import GalaxiaSerializer


class GalaxiaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Galaxia.objects.all()
    serializer_class = GalaxiaSerializer

    def get_queryset(self):
        usuario = self.request.user
        if usuario.groups.filter(name="Pesquisadores"):
            return Galaxia.objects.all()
        elif usuario.groups.filter(name="Administradores"):
            return Galaxia.objects.all()
