from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Always allow safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # If user has no profile, deny permission gracefully
        user_profile = getattr(request.user, 'userprofile', None)
        if user_profile is None:
            return False

        # Only allow if the user owns this community
        return obj.created_by == user_profile
