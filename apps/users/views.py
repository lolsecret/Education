from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from apps.users.models import Student
from apps.users.serializers import CreateCourceSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = CreateCourceSerializer