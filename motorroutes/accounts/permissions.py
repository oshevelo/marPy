from rest_framework import permissions
from .models import UserProfile


class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permissions for UserProfileDetails view to only allow
    user to edit their own profile. Otherwise, Get and Post Only.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        # 1/0
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return request.user == obj.user

        return False

