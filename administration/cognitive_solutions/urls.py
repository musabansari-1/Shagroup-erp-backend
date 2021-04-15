from django.urls import path, include

urlpatterns = [
    path('programs/', include('administration.cognitive_solutions.programs.urls'))
]