from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import FlashCard
from .serializers import FlashCardSerializer


class FlashCardView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlashCardSerializer
    queryset = FlashCard.objects.all()


class FlashCardItemView(RetrieveUpdateDestroyAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
