from django.shortcuts import render

# Create your views here.
from requests import Response
from rest_framework import generics
from django.views.generic.detail import DetailView

from apps.cources.models import Courses
from apps.cources.serializers import CourceSerializer


class CourceListView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourceSerializer


class CourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourceSerializer
