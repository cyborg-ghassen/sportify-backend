from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, TeamMembershipViewSet

routes = DefaultRouter()

routes.register(r'team', TeamViewSet, basename='team-team')
routes.register(r'team-membership', TeamMembershipViewSet, basename='team-membership')

urlpatterns = [
    *routes.urls
]
