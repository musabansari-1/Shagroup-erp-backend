from django.urls import include, path
from rest_framework import routers
from .views import *

app_name = 'expenses'

router = routers.DefaultRouter()
router.register(r'account_heads', AccountHeadViewSet)
router.register(r'expenses', ExpenseViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)), 
    path('statements/', StatementView.as_view())
]