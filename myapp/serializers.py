from .models import abcd
from rest_framework.serializers import ModelSerializer

class StudSeriazers(ModelSerializer):
    class Meta:
        model = abcd
        fields = ['id','name']