from rest_framework import permissions

class CheckStatus(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'owner':
            return True
        return False


class CheckRatings(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'client':
            return True
        return False


class CheckBooking(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == 'client':
            return True
        return False


class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == 'owner' and obj.room_number == 'owner':
            return False
        return True

