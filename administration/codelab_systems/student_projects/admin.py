from django.contrib import admin
from .models import SSLC, PUC, StudentProject, Trainer, TrainerRole
# Register your models here.

admin.site.register(SSLC)
admin.site.register(PUC)
admin.site.register(StudentProject)
admin.site.register(TrainerRole)
admin.site.register(Trainer)
