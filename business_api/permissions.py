from rest_framework import permissions


class AccessOwnProfile(permissions.BasePermission):
    """allow business to access data he/she has been provided"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to their own data"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
