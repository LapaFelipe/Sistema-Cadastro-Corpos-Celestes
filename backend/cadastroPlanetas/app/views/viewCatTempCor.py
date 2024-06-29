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

from app.models.CatTempCorModel import CatTempCor
from app.serializer.sCatTempCor import CatTempCorSerializer


class CatTempCorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CatTempCor.objects.all()
    serializer_class = CatTempCorSerializer

    def get_queryset(self):
        usuario = self.request.user
        if usuario.groups.filter(name="Pesquisadores"):
            return CatTempCor.objects.all()
        elif usuario.groups.filter(name="Administradores"):
                return CatTempCor.objects.all()
