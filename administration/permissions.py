from rest_framework.permissions import IsAdminUser 
from users.permissions import IsAdministration

PERMISSION_CLASSES_FOR_ADMINISTRATION = IsAdminUser | IsAdministration
