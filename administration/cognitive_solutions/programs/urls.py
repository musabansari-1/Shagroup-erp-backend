from django.urls import include, path
from rest_framework import routers
from .views import *

app_name = 'programs'

router = routers.DefaultRouter()
router.register(r'cognitive_internships', CognitiveInternshipViewSet)
router.register(r'academic_internships', AcademicInternshipViewSet)
router.register(r'employee_internships', EmployeeInternshipViewSet)
router.register(r'cognitive_workshops', CognitiveWorkshopViewSet)
router.register(r'academic_workshops', AcademicWorkshopViewSet)
router.register(r'colleges', CollegeViewSet)
router.register(r'companys', CompanyViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'streams', StreamViewSet)
router.register(r'frontends', FrontendViewSet)
router.register(r'backends', BackendViewSet)
router.register(r'internships', InternshipViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'workshops', WorkshopViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)), 
    path('overviews/', Overview.as_view())
]