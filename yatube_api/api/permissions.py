from rest_framework import permissions


class UserIsAuthor(permissions.BasePermission):
    """Permission - пользователь = автор."""
    message = 'У вас недостаточно прав для совершения действия'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
