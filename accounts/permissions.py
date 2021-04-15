from rest_framework.permissions import IsAdminUser 
from users.permissions import IsAccounts

PERMISSION_CLASSES_FOR_ACCOUNTS = IsAdminUser | IsAccounts
