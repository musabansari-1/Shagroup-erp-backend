from django.urls import path, include

urlpatterns = [
    path('fees/', include('accounts.all.fees.urls')),
    path('expenses/', include('accounts.all.expenses.urls'))
]