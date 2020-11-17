from rest_framework import serializers
from .models import *

class pgownerSerializers(serializers.ModelSerializer):
    class Meta:
        model=pgowner
        fields='__all__'
