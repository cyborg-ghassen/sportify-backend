from rest_framework.permissions import BasePermission


class ViewAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user and "admin" in [group.name for group in request.user.groups.all()]:
            return True

        return False


class ViewCoach(BasePermission):
    def has_permission(self, request, view):
        if request.user and "coach" in [group.name for group in request.user.groups.all()]:
            return True

        return False


class ViewPlayer(BasePermission):
    def has_permission(self, request, view):
        if request.user and "player" in [group.name for group in request.user.groups.all()]:
            return True

        return False


class ViewVisitor(BasePermission):
    def has_permission(self, request, view):
        if request.user and "visitor" in [group.name for group in request.user.groups.all()]:
            return True

        return False


class ViewAdherent(BasePermission):
    def has_permission(self, request, view):
        if request.user and "adherent" in [group.name for group in request.user.groups.all()]:
            return True

        return False
