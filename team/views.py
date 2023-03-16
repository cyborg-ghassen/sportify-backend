from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Team, TeamMembership
from .serializers import TeamSerializer, TeamMembershipSerializer


# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = [IsAuthenticated]


class TeamMembershipViewSet(viewsets.ModelViewSet):
    serializer_class = TeamMembershipSerializer
    queryset = TeamMembership.objects.all()
    permission_classes = [IsAuthenticated]
