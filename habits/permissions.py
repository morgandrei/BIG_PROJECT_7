from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    message = 'Вы не являетесь администратором'

    def has_object_permission(self, request, view, obj):
        if request.user == request.user.is_superuser:
            return True
        return False


class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцем'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or obj.is_public:
            return True
        return False
