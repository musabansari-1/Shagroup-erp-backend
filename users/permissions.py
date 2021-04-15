from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser
from .models import User

class IsAdministration(BasePermission):
    """
    Allows access only to users of department of administration.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and 
            request.user.department == User.ADMINISTRATION
        )

class IsAdministrationReadCreate(BasePermission):
    """
    Allows only read and create access only to users of department of administration.
    """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and
            request.user and request.user.is_authenticated and 
            request.user.department == User.ACCOUNTS
        )

class IsAccounts(BasePermission):
    """
    Allows access only to users of department of accounts.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and 
            request.user.department == User.ACCOUNTS
            )

class IsAccountsSafe(BasePermission):
    """
    Allows read-only access only to users of department of administration.
    """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and
            request.user and request.user.is_authenticated and 
            request.user.department == User.ACCOUNTS
        )