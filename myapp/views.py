from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .serializers import StudSeriazers
from .models import abcd
# Create your views here.

class StudentView(ListCreateAPIView):
    queryset=abcd.objects.all()
    serializer_class=StudSeriazers

