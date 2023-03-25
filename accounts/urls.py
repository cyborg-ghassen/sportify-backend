from rest_framework.routers import DefaultRouter

from .views import LoginViewSet, RegistrationViewSet, RefreshViewSet, UserViewSet, GroupViewSet, \
    PermissionViewSet

routes = DefaultRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')
routes.register(r'group', GroupViewSet, basename='group')
routes.register(r'permission', PermissionViewSet, basename='permission')

urlpatterns = [
    *routes.urls
]
