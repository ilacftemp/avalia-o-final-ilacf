from rest_framework import serializers
from .models import Filme, FunFacts, Anuncio


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['id', 'title', 'palavras']

class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunFacts
        fields = ['id', 'fact']

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = ['id', 'headline', 'img', 'link']