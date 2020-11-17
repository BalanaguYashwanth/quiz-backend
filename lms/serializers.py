from rest_framework import serializers
from .models import *

class verifySerializers(serializers.ModelSerializer):
    class Meta:
        model=verify
        fields='__all__'

class quizSerializers(serializers.ModelSerializer):
    class Meta:
        model=quiz
        fields='__all__'