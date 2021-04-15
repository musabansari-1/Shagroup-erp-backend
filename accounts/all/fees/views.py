from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from .models import * 
from .serializers import * 
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import views
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from administration.cognitive_solutions.programs.models import *
from accounts.permissions import PERMISSION_CLASSES_FOR_ACCOUNTS 
from users.permissions import IsAdministrationReadCreate
from django.db.models import F
from django.db.models.query import QuerySet

class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer 
    # permission_classes = [ permissions_classes_for_accounts ]
    permission_classes = [ PERMISSION_CLASSES_FOR_ACCOUNTS ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',] 

class CognitiveInternshipFeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CognitiveInternshipFees.objects.all()
    serializer_class = CognitiveInternshipFeesSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | IsAdministration | permissions.IsAdminUser)]
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | permissions.IsAdminUser)]
    # permission_classes = [ permissions_classes_for_accounts | IsAdministrationReadCreate ]
    permission_classes = [ PERMISSION_CLASSES_FOR_ACCOUNTS | IsAdministrationReadCreate ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['date', 'received_from']
    search_fields = ['receipt_no', 'received_from__name' , 'received_from__register_no']
    ordering = ['receipt_no',]

class AcademicInternshipFeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AcademicInternshipFees.objects.all()
    serializer_class = AcademicInternshipFeesSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | IsAdministration | permissions.IsAdminUser)]
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | permissions.IsAdminUser)]
    # permission_classes = [ permissions_classes_for_accounts | IsAdministrationReadCreate ]
    permission_classes = [ PERMISSION_CLASSES_FOR_ACCOUNTS | IsAdministrationReadCreate ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['date', 'received_from']
    search_fields = ['receipt_no','received_from__name', 'received_from__register_no']
    ordering = ['receipt_no',]

class EmployeeInternshipFeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeInternshipFees.objects.all()
    serializer_class = EmployeeInternshipFeesSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | permissions.IsAdminUser)]
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | IsAdministration | permissions.IsAdminUser)]
    # permission_classes = [ permissions_classes_for_accounts | IsAdministrationReadCreate ]
    permission_classes = [ PERMISSION_CLASSES_FOR_ACCOUNTS | IsAdministrationReadCreate ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['date', 'received_from']
    search_fields = ['receipt_no','received_from__name', 'received_from__register_no']
    ordering = ['receipt_no',]

class CognitiveWorkshopFeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CognitiveWorkshopFees.objects.all()
    serializer_class = CognitiveWorkshopFeesSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | permissions.IsAdminUser)]
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | IsAdministration | permissions.IsAdminUser)]
    # permission_classes = [ permissions_classes_for_accounts | IsAdministrationReadCreate ]
    permission_classes = [ PERMISSION_CLASSES_FOR_ACCOUNTS | IsAdministrationReadCreate ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['date', 'received_from']
    search_fields = ['receipt_no', 'received_from__name' , 'received_from__register_no']
    ordering = ['receipt_no',]

class AcademicWorkshopFeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AcademicWorkshopFees.objects.all()
    serializer_class = AcademicWorkshopFeesSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | permissions.IsAdminUser)]
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | IsAdministration | permissions.IsAdminUser)]
    # permission_classes = [ permissions_classes_for_accounts | IsAdministrationReadCreate ]
    permission_classes = [ PERMISSION_CLASSES_FOR_ACCOUNTS | IsAdministrationReadCreate ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['date', 'received_from']
    search_fields = ['receipt_no','received_from__name', 'received_from__register_no']
    ordering = ['receipt_no',]

class StudentProjectFeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = StudentProjectFees.objects.all()
    serializer_class = StudentProjectFeesSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | permissions.IsAdminUser)]
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | IsAdministration | permissions.IsAdminUser)]
    # permission_classes = [ permissions_classes_for_accounts | IsAdministrationReadCreate ]
    permission_classes = [ PERMISSION_CLASSES_FOR_ACCOUNTS | IsAdministrationReadCreate ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['date', 'received_from']
    search_fields = ['receipt_no','received_from__name', 'received_from__register_no']
    ordering = ['receipt_no',]

class StudentProjectCollegewiseViewSet(viewsets.ViewSet):
    """
    Returns empty list if no college_id is passed.
    Returns list of projects under particular college if college_id is passed.
    Returns list of student with calculated balance if both college_id and project_id is passed.  
    """
    # permission_classes = [ permissions_classes_for_accounts ]
    permission_classes = [ PERMISSION_CLASSES_FOR_ACCOUNTS ]

    def list(self, request):
        college_id = request.GET.get('college_id', None) 
        project_id = request.GET.get('project_id', None) 

        if college_id:
            if not project_id:
                students = StudentProject.objects.filter(college=college_id)
                projects = []
                for student in students:
                    print(student)
                    project_id = student.project.id 
                    project_title= student.project.title
                    project = {"id": project_id, "title": project_title}
                    if project not in projects:
                        projects.append(project)
                return Response(projects)
        else:
            return Response([])

        queryset = StudentProjectFees.objects.filter(received_from__college__id=college_id, received_from__project__id=project_id).values_list('id', 'received_from')
        unique_id = {} 

        for id,received_from in queryset:
            unique_id[received_from] = id

        queryset = StudentProjectFees.objects.filter(id__in=unique_id.values())
        serializer = StudentProjectFeesBalanceSerializer(queryset, many=True)
        # if request.GET.get('reverse', None) == '1':
        #     sorted_q = sorted(serializer.data, key=lambda x: x['balance'], reverse=True)
        #     return Response(sorted_q)

        return Response(serializer.data)

class BatchwiseStudentView(views.APIView):
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts| permissions.IsAdminUser)]
    # permission_classes = [ permissions_classes_for_accounts ]
    permission_classes = [ PERMISSION_CLASSES_FOR_ACCOUNTS ]

    def get(self, request, format=None):
        if request.GET.get('batch', '') == '':
            raise ParseError(detail='batch couldn\'t be parsed from url.')           
        else:
            try:
                batch_id = int(request.GET['batch'])
            except ValueError:
                raise ParseError(detail='batch must be integer value.')           

        ai_students = AcademicInternship.objects.filter(batch__id=batch_id)
        ci_students = CognitiveInternship.objects.filter(batch__id=batch_id)
        ei_students = EmployeeInternship.objects.filter(batch__id=batch_id)
        students = []

        for ai_student in ai_students:
            fees = AcademicInternshipFees.objects.filter(received_from=ai_student)
            actual_fees = ai_student.batch.internship.actual_fees - ai_student.concession
            paid = 0
            for fee in fees:
                paid += fee.amount
            balance = actual_fees - paid
            student = {
                "id":ai_student.id,"profile_pic":ai_student.profile_pic.url,"register_no": ai_student.register_no, 
                "name": ai_student.name, "contact_1": ai_student.contact_1, 
                "contact_2": ai_student.contact_2, "actual_fees": actual_fees, 
                "paid": paid, "balance":balance
                }
            students.append(student)
            

        for ci_student in ci_students:
            fees = CognitiveInternshipFees.objects.filter(received_from=ci_student)
            actual_fees = ci_student.batch.internship.actual_fees - ci_student.concession
            paid = 0
            for fee in fees:
                paid += fee.amount
            balance = actual_fees - paid
            student = {
                "id":ci_student.id,"profile_pic":ci_student.profile_pic.url,"register_no": ci_student.register_no, 
                "name": ci_student.name, "contact_1": ci_student.contact_1, 
                "contact_2": ci_student.contact_2, "actual_fees": actual_fees, 
                "paid": paid, "balance":balance
                }
            students.append(student)

        for ei_student in ei_students:
            fees = EmployeeInternshipFees.objects.filter(received_from=ei_student)
            actual_fees = ei_student.batch.internship.actual_fees - ei_student.concession
            paid = 0
            for fee in fees:
                paid += fee.amount
            balance = actual_fees - paid
            student = {
                "id":ei_student.id,"profile_pic":ei_student.profile_pic.url,"register_no": ei_student.register_no, 
                "name": ei_student.name, "contact_1": ei_student.contact_1, 
                "contact_2": ei_student.contact_2, "actual_fees": actual_fees, 
                "paid": paid, "balance":balance
                }
            students.append(student)

        students = sorted(students, key = lambda student: (student['name']))

        return Response(students)


class WorkshopStudentView(views.APIView):
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | permissions.IsAdminUser)] 
    # permission_classes = [ permissions_classes_for_accounts ]
    permission_classes = [ PERMISSION_CLASSES_FOR_ACCOUNTS ]

    def get(self, request, format=None):
        if request.GET.get('workshop', '') == '':
            raise ParseError(detail='workshop couldn\'t be parsed from url.')           
        else:
            try:
                workshop_id = int(request.GET['workshop'])
            except ValueError:
                raise ParseError(detail='workshop must be integer value.')           

        ai_students = AcademicWorkshop.objects.filter(workshop__id=workshop_id)
        ci_students = CognitiveWorkshop.objects.filter(workshop__id=workshop_id)
        students = []

        for ai_student in ai_students:
            fees = AcademicWorkshopFees.objects.filter(received_from=ai_student)
            actual_fees = ai_student.workshop.actual_fees - ai_student.concession
            paid = 0
            for fee in fees:
                paid += fee.amount
            balance = actual_fees - paid
            student = {
                "id":ai_student.id,"profile_pic":ai_student.profile_pic.url,"register_no": ai_student.register_no, 
                "name": ai_student.name, "contact_1": ai_student.contact_1, 
                "contact_2": ai_student.contact_2, "actual_fees": actual_fees, 
                "paid": paid, "balance":balance
                }
            students.append(student)
            

        for ci_student in ci_students:
            fees = CognitiveWorkshopFees.objects.filter(received_from=ci_student)
            actual_fees = ci_student.workshop.actual_fees - ci_student.concession
            paid = 0
            for fee in fees:
                paid += fee.amount
            balance = actual_fees - paid
            student = {
                "id":ci_student.id,"profile_pic":ci_student.profile_pic.url,"register_no": ci_student.register_no, 
                "name": ci_student.name, "contact_1": ci_student.contact_1, 
                "contact_2": ci_student.contact_2, "actual_fees": actual_fees, 
                "paid": paid, "balance":balance
                }
            students.append(student)

        students = sorted(students, key = lambda student: (student['name']))

        return Response(students)