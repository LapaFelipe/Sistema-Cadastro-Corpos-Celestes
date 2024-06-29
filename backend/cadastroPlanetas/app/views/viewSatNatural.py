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

from app.models.SatNaturalModel import SatNatural
from app.serializer.sSatNatural import SatNaturalSerializer


class SatNaturalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SatNatural.objects.all()
    serializer_class = SatNaturalSerializer

    def get_queryset(self):
        usuario = self.request.user
        if usuario.groups.filter(name="Pesquisadores"):
            return SatNatural.objects.all()
        elif usuario.groups.filter(name="Administradores"):
            return SatNatural.objects.all()
