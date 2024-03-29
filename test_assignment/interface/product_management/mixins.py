from django.contrib.auth import get_permission_codename


class PermissionMixin(object):
    """
    Mixin to check if user has permission to perform action
    """

    def has_product_add_permission(self, request):
        """
        Return True if the given request has permission to add an object.
        Can be overridden by the user in subclasses.
        """
        opts = self.model._meta
        codename = get_permission_codename("add", opts)

        return request.user.has_perm("%s.%s" % (opts.app_label, codename)) or request.user.is_staff

    def has_change_permission(self, request, obj=None):
        """
        Return True if the given request has permission to change an object.
        Can be overridden by the user in subclasses.
        """
        opts = self.model._meta
        codename = get_permission_codename("change", opts)

        return request.user.has_perm("%s.%s" % (opts.app_label, codename)) or request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        """
        Return True if the given request has permission to delete an object.
        Can be overridden by the user in subclasses.
        """
        opts = self.model._meta
        codename = get_permission_codename("delete", opts)

        return request.user.has_perm("%s.%s" % (opts.app_label, codename)) or request.user.is_staff
