from django.urls import path, include

urlpatterns = [
    path('student_projects/', include('administration.codelab_systems.student_projects.urls'))
]