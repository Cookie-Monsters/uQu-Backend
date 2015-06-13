from api.models import Answer, Question, User
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User