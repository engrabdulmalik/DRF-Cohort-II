from django.shortcuts import render
from .models import *
from rest_framework.generics import ListAPIView
from .serializer import SchoolSerializer

# Create your views here.

class SchoolList(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

