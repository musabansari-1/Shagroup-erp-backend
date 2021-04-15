from django.urls import include, path
from rest_framework import routers
from .views import *

app_name = 'fees'

router = routers.DefaultRouter()
router.register(r'payment_type', PaymentTypeViewSet)
router.register(r'cognitive_internship_fees', CognitiveInternshipFeesViewSet)
router.register(r'academic_internship_fees', AcademicInternshipFeesViewSet)
router.register(r'employee_internship_fees', EmployeeInternshipFeesViewSet)
router.register(r'cognitive_workshop_fees', CognitiveWorkshopFeesViewSet)
router.register(r'academic_workshop_fees', AcademicWorkshopFeesViewSet)
router.register(r'student_project_fees', StudentProjectFeesViewSet)
router.register(r'student_project_collegewise', StudentProjectCollegewiseViewSet, basename='balance')



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('batchwise_students/', BatchwiseStudentView.as_view()),
    path('workshop_students/', WorkshopStudentView.as_view())

]