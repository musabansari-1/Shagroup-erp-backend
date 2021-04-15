from django.urls import include, path
from rest_framework import routers
from .views import *

app_name = 'student_projects'

router = routers.DefaultRouter()
router.register(r'sslcs', SSLCViewSet)
router.register(r'pucs', PUCViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'trainer_roles', TrainerRoleViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'student_projects', StudentProjectViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)), 
    path('college_overview/', CollegeOverview.as_view()), 
    path('student_project_overview/', StudentProjectOverview.as_view()), 
]