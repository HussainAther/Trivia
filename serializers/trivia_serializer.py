from rest_framework import serializers
from .models import Trivia

class TriviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trivia
        fields = ['id', 'category', 'question', 'answer', 'user']


