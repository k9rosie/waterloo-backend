from rest_framework import permissions


class IsEditorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.has_perms(self, ('reviews.change_review',
                                             'reviews.delete_review',
                                             'reviews.add_review',))
