from rest_framework.routers import DefaultRouter

from .views import SportViewSet, EquipmentViewSet, VenueViewSet, TrainingRoomViewSet, InfrastructureViewSet

routes = DefaultRouter()

routes.register(r'sport', SportViewSet, basename='structure-sport')
routes.register(r'equipment', EquipmentViewSet, basename='structure-equipment')
routes.register(r'venue', VenueViewSet, basename='structure-venue')
routes.register(r'training-room', TrainingRoomViewSet, basename='structure-training')
routes.register(r'infrastructure', InfrastructureViewSet, basename='structure-infrastructure')

urlpatterns = [
    *routes.urls
]
