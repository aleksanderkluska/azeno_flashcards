from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from .models import FlashCard, Deck, Tag, DifficultyLevel


class FlashCardSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('id',
                  'question',
                  'answer',
                  'author',
                  'category',
                  'difficulty',
                  'rating',
                  'tags',
                  'deck')


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email',)


class DifficultyLevelSerializer(ModelSerializer):
    class Meta:
        model = DifficultyLevel
        fields = ('name', 'value')


class DeckSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    author = AuthorSerializer()
    difficulty = DifficultyLevelSerializer()

    class Meta:
        model = Deck
        fields = ('id',
                  'author',
                  'name',
                  'category',
                  'difficulty',
                  'rating',
                  'tags',
                  'description',
                  'is_public',
                  )
