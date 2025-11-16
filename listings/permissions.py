from rest_framework import permissions

class IsCommunityMemberOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Must be authenticated
        if not request.user.is_authenticated:
            return False

        community = view.kwargs.get('community_id')

        # Check if user is a member
        return request.user.userprofile.communities.filter(id=community).exists()
