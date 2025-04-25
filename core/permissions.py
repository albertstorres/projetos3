from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user

        if hasattr(obj, 'account_id'):
            return obj.account_id and obj.account_id == user.id

        return False