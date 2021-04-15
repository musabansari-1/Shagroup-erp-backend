from django.db.models.query import InstanceCheckMeta
from rest_framework import views
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from rest_framework.response import Response
from .models import * 
from .serializers import * 
# from django_filters.rest_framework import DjangoFilterBackend
from url_filter.integrations.drf import DjangoFilterBackend
from administration.permissions import PERMISSION_CLASSES_FOR_ADMINISTRATION 
from users.permissions import IsAccountsSafe

class CognitiveInternshipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CognitiveInternship.objects.all()
    serializer_class = CognitiveInternshipSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | IsAccountsSafe | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION | IsAccountsSafe ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['batch',]
    search_fields = ['name',]
    ordering = ['register_no',]

 
class AcademicInternshipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AcademicInternship.objects.all()
    serializer_class = AcademicInternshipSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | IsAccountsSafe | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION | IsAccountsSafe ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['batch',]
    search_fields = ['name',]
    ordering = ['register_no',]

class EmployeeInternshipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeInternship.objects.all()
    serializer_class = EmployeeInternshipSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | IsAccountsSafe | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION | IsAccountsSafe ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['batch',]
    search_fields = ['name',]
    ordering = ['register_no',]

class CognitiveWorkshopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CognitiveWorkshop.objects.all()
    serializer_class = CognitiveWorkshopSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | IsAccountsSafe | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION | IsAccountsSafe ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['register_no',]

class AcademicWorkshopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AcademicWorkshop.objects.all()
    serializer_class = AcademicWorkshopSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | IsAccountsSafe | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION | IsAccountsSafe ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['register_no',]


class CollegeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = College.objects.all()
    serializer_class = CollegeSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]


class FrontendViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Frontend.objects.all()
    serializer_class = FrontendSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]


class BackendViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Backend.objects.all()
    serializer_class = BackendSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]

class InternshipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]

class BatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['internship',]
    search_fields = ['name',]
    ordering = ['name',]

class WorkshopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]

class StreamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'course__name',]
    ordering = ['name',]


class Overview(views.APIView):
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]

    def get(self, request, format=None):
        ci = CognitiveInternship.objects.all()
        ai = AcademicInternship.objects.all()
        ei = EmployeeInternship.objects.all()
        cw = CognitiveWorkshop.objects.all()
        aw = AcademicInternship.objects.all()
        ci_students = ci.count()
        ai_students = ai.count()
        ei_employees = ei.count()
        cw_students = cw.count()
        aw_students = aw.count()
        ci_colleges = ci.values('college').distinct().count()
        ai_colleges = ai.values('college').distinct().count()
        ei_companys= ei.values('company').distinct().count()
        cw_colleges = cw.values('college').distinct().count()
        aw_colleges = aw.values('college').distinct().count()
        total = ci_students + ai_students + ei_employees + cw_students + aw_students

        data = {"ci_students": ci_students, "ai_students": ai_students, 
        "ei_employees": ei_employees,"cw_students": cw_students, "aw_students": aw_students,
        "ci_colleges": ci_colleges, "ai_colleges": ai_colleges, 
        "ei_companys": ei_companys,"cw_colleges": cw_colleges, "aw_colleges": aw_colleges,
        "total": total} 
        return Response(data)