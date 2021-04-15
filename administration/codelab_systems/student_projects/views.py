from rest_framework import views
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from django.db.models import QuerySet
from .models import * 
from .serializers import * 
from users.permissions import IsAccountsSafe
from url_filter.integrations.drf import DjangoFilterBackend
from administration.permissions import PERMISSION_CLASSES_FOR_ADMINISTRATION
from administration.cognitive_solutions.programs.models import College
from rest_framework.response import Response

class SSLCViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SSLC.objects.all()
    serializer_class = SSLCSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]


class PUCViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PUC.objects.all()
    serializer_class = PUCSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]


class TrainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]

class TrainerRoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TrainerRole.objects.all()
    serializer_class = TrainerRoleSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | IsAccountsSafe | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION | IsAccountsSafe ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title',]
    ordering = ['title',]

class StudentProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = StudentProject.objects.all()
    serializer_class = StudentProjectSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | IsAccountsSafe | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION | IsAccountsSafe ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name',]
    filter_fields = ['college', 'project']
    ordering = ['register_no',]

class CollegeOverview(views.APIView):
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]

    def get(self, request, format=None):
        colleges = College.objects.all()
        data = []
        total_no_of_students = 0
        for college in colleges:
            no_of_students = StudentProject.objects.filter(college=college).count()
            total_no_of_students += no_of_students
            dictionary = {'college_id': college.id, 'college_name': college.name, 'state': college.state, 'district': college.district, 'no_of_students': no_of_students}
            data.append(dictionary)
        response = {'total_no_of_students': total_no_of_students, 'colleges': data}
        return Response(response)
    
    
class StudentProjectOverview(views.APIView):
    # permission_classes = [permissions.IsAuthenticated & (IsAdministration | permissions.IsAdminUser)]
    permission_classes = [PERMISSION_CLASSES_FOR_ADMINISTRATION]

    def get(self, request, format=None):
        college_id = request.GET.get('college_id', None)
        if not college_id:
            return Response([])
        projects = Project.objects.all()
        lst = []
        for project in projects:
            students = StudentProject.objects.filter(college__id=college_id, project=project)
            if not students:
                continue
            project_name = project.title
            stds = []
            for student in students:
                dictionary = {'register_no':student.register_no, 'name': student.name, 'contact_1': student.contact_1, 'contact_2':student.contact_2}
                stds.append(dictionary)
            data = {'project_name':project_name, 'students':stds}
            lst.append(data)
            lst = sorted(lst, key = lambda project: (project['project_name']))
        return Response(lst)
        # students_query = StudentProject.objects.filter(college__id=college_id).query
        # students_query.group_by = ['project__title']
        # students_query.order_by = ['project__title']
        # students = QuerySet(query=students_query, model=StudentProject)
        # lists = []
        # print(students)
        # for student in students:
        #     dictionary = {'register_no':student.register_no, 'name': student.name, 'contact_1': student.contact_1, 'contact_2':student.contact_2,'project': student.project.title}
        #     lists.append(dictionary)
        # return Response(lists)
        # data = []
        # total_no_of_students = 0
        # for college in colleges:
        #     no_of_students = StudentProject.objects.filter(college=college)
        #     total_no_of_students += no_of_students
        #     dictionary = {'college_id': college.id, 'college_name': college.name, 'state': college.state, 'district': college.district, 'no_of_students': no_of_students}
        #     data.append(dictionary)
        # response = {'total_no_of_students': total_no_of_students, 'colleges': data}
        # return Response(response