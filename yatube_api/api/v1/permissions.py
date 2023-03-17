from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a author, or is a read-only request.
    """
    message = {'errors': ['You ate not the author of this content.']}

    def has_object_permission(self, request, view, obj):
        self.message['errors'].clear()
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
