from django.urls import path, include

urlpatterns = [
    path('cognitive_solutions/', include('administration.cognitive_solutions.urls')),
    path('codelab_systems/', include('administration.codelab_systems.urls'))
]