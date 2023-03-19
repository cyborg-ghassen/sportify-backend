from rest_framework.permissions import BasePermission


class ViewAdmin(BasePermission):
    def has_permission(self, request, view):
        if "admin" in request.user.groups.all():
            return True

        return False


class ViewCoach(BasePermission):
    def has_permission(self, request, view):
        if "coach" in request.user.groups.all():
            return True

        return False


class ViewPlayer(BasePermission):
    def has_permission(self, request, view):
        if "player" in request.user.groups.all():
            return True

        return False


class ViewVisitor(BasePermission):
    def has_permission(self, request, view):
        if "visitor" in request.user.groups.all():
            return True

        return False


class ViewAdherent(BasePermission):
    def has_permission(self, request, view):
        if "adherent" in request.user.groups.all():
            return True

        return False
