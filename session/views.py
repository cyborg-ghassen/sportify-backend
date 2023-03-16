from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Match, Participation, TrainingSession
from .serializers import MatchSerializer, ParticipationSerializer, TrainingSessionSerializer


# Create your views here.
class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
    permission_classes = [IsAuthenticated]


class ParticipationViewSet(viewsets.ModelViewSet):
    serializer_class = ParticipationSerializer
    queryset = Participation.objects.all()
    permission_classes = [IsAuthenticated]


class TrainingSessionViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingSessionSerializer
    queryset = TrainingSession.objects.all()
    permission_classes = [IsAuthenticated]
