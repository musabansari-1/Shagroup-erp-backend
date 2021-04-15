from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PaymentType)
admin.site.register(CognitiveInternshipFees)
admin.site.register(AcademicInternshipFees)
admin.site.register(EmployeeInternshipFees)
admin.site.register(CognitiveWorkshopFees)
admin.site.register(AcademicWorkshopFees)
admin.site.register(StudentProjectFees)
