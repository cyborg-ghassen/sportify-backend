from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from utils.permission import ViewAdmin, ViewVisitor, ViewAdherent, ViewCoach
from .models import Sport, Equipment, Venue, TrainingRoom, Infrastructure
from .serializers import SportSerializer, EquipmentSerializer, VenueSerializer, TrainingRoomSerializer, \
    InfrastructureSerializer


# Create your views here.
class SportViewSet(viewsets.ModelViewSet):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()
    permission_classes = [ViewAdmin | ViewVisitor | ViewAdherent]


class EquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()
    permission_classes = [ViewAdmin]


class VenueViewSet(viewsets.ModelViewSet):
    serializer_class = VenueSerializer
    queryset = Venue.objects.all()
    permission_classes = [ViewAdmin]


class TrainingRoomViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingRoomSerializer
    queryset = TrainingRoom.objects.all()
    permission_classes = [ViewAdmin | ViewCoach]


class InfrastructureViewSet(viewsets.ModelViewSet):
    serializer_class = InfrastructureSerializer
    queryset = Infrastructure.objects.all()
    permission_classes = [ViewAdmin | ViewVisitor]
