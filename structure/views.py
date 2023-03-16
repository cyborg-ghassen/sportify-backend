from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Sport, Equipment, Venue, TrainingRoom, Infrastructure
from .serializers import SportSerializer, EquipmentSerializer, VenueSerializer, TrainingRoomSerializer, \
    InfrastructureSerializer


# Create your views here.
class SportViewSet(viewsets.ModelViewSet):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()
    permission_classes = [IsAuthenticated]


class EquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()
    permission_classes = [IsAuthenticated]


class VenueViewSet(viewsets.ModelViewSet):
    serializer_class = VenueSerializer
    queryset = Venue.objects.all()
    permission_classes = [IsAuthenticated]


class TrainingRoomViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingRoomSerializer
    queryset = TrainingRoom.objects.all()
    permission_classes = [IsAuthenticated]


class InfrastructureViewSet(viewsets.ModelViewSet):
    serializer_class = InfrastructureSerializer
    queryset = Infrastructure.objects.all()
    permission_classes = [IsAuthenticated]
