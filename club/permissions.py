from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        authenticated = request.user.is_authenticated
        super_user = request.user.is_superuser
        return authenticated and super_user