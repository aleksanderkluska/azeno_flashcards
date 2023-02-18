from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from . import models, serializers, paginations
from .permissions import IsAuthor


class DeckViewSet(ModelViewSet):
    queryset = models.Deck.objects.select_related('difficulty', 'author').all()
    pagination_class = paginations.CustomPagination
    serializer_class = serializers.DeckSerializer

    def list(self, request, *args, **kwargs):
        # serializer = serializers.DeckSerializer(self.queryset, many=True)
        # return Response(serializer.data)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, pk=None, **kwargs):
        deck = get_object_or_404(queryset=self.queryset, pk=pk)
        serializer = serializers.DeckSerializer(deck)
        return Response(serializer.data)


class DeckOwnerViewSet(ViewSet):
    permission_classes = [IsAuthenticated, IsAuthor]
    queryset = models.Deck.objects.all()

    def list(self, request):
        deck = self.queryset.filter(author=request.user)
        serializer = serializers.DeckSerializer(deck, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        deck = get_object_or_404(queryset=self.queryset, pk=pk)
        self.check_object_permissions(request, deck)
        serializer = serializers.DeckSerializer(deck)
        return Response(serializer.data)

