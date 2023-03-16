from rest_framework.routers import DefaultRouter

from .views import ParticipationViewSet, TrainingSessionViewSet, MatchViewSet

routes = DefaultRouter()

routes.register(r'participation', ParticipationViewSet, basename='session-participation')
routes.register(r'training', TrainingSessionViewSet, basename='session-training')
routes.register(r'match', MatchViewSet, basename='session-match')

urlpatterns = [
    *routes.urls
]
