from rest_framework.permissions import BasePermission


class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        authenticated = request.user.is_authenticated
        staff_user = request.user.is_staff
        return authenticated and staff_user


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        authenticated = request.user.is_authenticated
        super_user = request.user.is_superuser
        return authenticated and super_user


class IsMember(BasePermission):
    def has_permission(self, request, view):
        authenticated = request.user.is_authenticated
        member = request.user.is_member
        return authenticated and member