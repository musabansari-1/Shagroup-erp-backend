from django.urls import path, include

urlpatterns = [
    path('all/', include('accounts.all.urls')),
]