from accounts.all.fees.models import AcademicInternshipFees, AcademicWorkshopFees, CognitiveInternshipFees, CognitiveWorkshopFees, EmployeeInternshipFees, StudentProjectFees
from administration.cognitive_solutions.programs.models import CognitiveInternship
from django.db.models.query import InstanceCheckMeta
from rest_framework import views
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from rest_framework.response import Response
from .models import * 
from .serializers import * 
# from users.permissions import IsAccounts
from datetime import datetime
from calendar import monthrange
from rest_framework.exceptions import ParseError
from utils.utils import validate_date_range
from url_filter.integrations.drf import DjangoFilterBackend
from accounts.permissions import PERMISSION_CLASSES_FOR_ACCOUNTS 
# PERMISSION_CLASSES_FOR_ACCOUNTS
class AccountHeadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AccountHead.objects.all()
    serializer_class = AccountHeadSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | permissions.IsAdminUser)]
    # permission_classes = [permissions_classes_for_accounts]
    permission_classes = [PERMISSION_CLASSES_FOR_ACCOUNTS]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering = ['name',]

class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer 
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts | permissions.IsAdminUser)]
    # permission_classes = [permissions_classes_for_accounts]
    permission_classes = [PERMISSION_CLASSES_FOR_ACCOUNTS]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['paid_date',]
    search_fields = ['account_head__name',]
    ordering = ['paid_date',]

class StatementView(views.APIView):
    # permission_classes = [permissions.IsAuthenticated & (IsAccounts| permissions.IsAdminUser)]
    # permission_classes = [permissions_classes_for_accounts]
    permission_classes = [PERMISSION_CLASSES_FOR_ACCOUNTS]

    def get(self, request, format=None):

        # print(request.GET['from_date'], request.GET['to_date'])
        if request.GET.get('from_date', '') != '' and request.GET.get('to_date', '') != '':
            try:
                from_date = datetime.strptime(request.GET['from_date'], '%Y-%m-%d').date()
                to_date = datetime.strptime(request.GET['to_date'], '%Y-%m-%d').date()
                validate_date_range(from_date=from_date, to_date=to_date)
                # if from_date > to_date:
                #     raise ParseError(detail="from_date must be less than to_date")           

            except ValueError:
                raise ParseError(detail="invalid date format. (format should be in 'YYYY-MM-DD')")           
        else:
        # datetime.today().replace(day=1)
            today = datetime.today()
            from_date = datetime(today.year, today.month, 1).date()
            to_date = datetime(today.year, today.month, monthrange(today.year,today.month)[1]).date()

        #calculating opening balance
        opening_balance = 0 
        expense_list = Expense.objects.filter(paid_date__lt=from_date)
        ci_fees_list = CognitiveInternshipFees.objects.filter(date__lt=from_date)
        ai_fees_list = AcademicInternshipFees.objects.filter(date__lt=from_date)
        ei_fees_list = EmployeeInternshipFees.objects.filter(date__lt=from_date)
        cw_fees_list = CognitiveWorkshopFees.objects.filter(date__lt=from_date)
        aw_fees_list = AcademicWorkshopFees.objects.filter(date__lt=from_date)
        sp_fees_list = StudentProjectFees.objects.filter(date__lt=from_date)
        for expense in expense_list:
            opening_balance -= expense.paid_amount

        # print(opening_balance) 
        for ci_fees in ci_fees_list:
            opening_balance += ci_fees.amount
        for ai_fees in ai_fees_list:
            opening_balance += ai_fees.amount
        # print(opening_balance) 
        for ei_fees in ci_fees_list:
            opening_balance += ei_fees.amount
        # print(opening_balance) 
        for cw_fees in ci_fees_list:
            opening_balance += cw_fees.amount
        for aw_fees in ai_fees_list:
            opening_balance += aw_fees.amount
        for sp_fees in sp_fees_list:
            opening_balance += sp_fees.amount

        # expense_list = Expense.objects.filter(paid_date__gte=from_date, paid_date__lte=to_date)
        expense_list = Expense.objects.filter(paid_date__range = [from_date, to_date])
        ci_fees_list = CognitiveInternshipFees.objects.filter(date__range = [from_date, to_date])
        ai_fees_list = AcademicInternshipFees.objects.filter(date__range = [from_date, to_date])
        ei_fees_list = EmployeeInternshipFees.objects.filter(date__range = [from_date, to_date])
        cw_fees_list = CognitiveWorkshopFees.objects.filter(date__range = [from_date, to_date])
        aw_fees_list = AcademicWorkshopFees.objects.filter(date__range = [from_date, to_date])
        sp_fees_list = StudentProjectFees.objects.filter(date__range = [from_date, to_date])


        statements = []
        closing_balance = opening_balance
        for expense in expense_list:
            closing_balance -= expense.paid_amount
            statement = {"date": expense.paid_date, "account_head": expense.account_head.name, "description": expense.description, "debit":None, "credit":expense.paid_amount}
            statements.append(statement)
        for ci_fees in ci_fees_list:
            closing_balance += ci_fees.amount
            statement = {"date": ci_fees.date, "account_head": "Cognitive Internship Fees", "description": ci_fees.receipt_no + "-" + ci_fees.received_from.name, "debit":ci_fees.amount, "credit":None}
            statements.append(statement)
        for ai_fees in ai_fees_list:
            closing_balance += ai_fees.amount
            statement = {"date": ai_fees.date, "account_head": "Academic Internship Fees","description": ai_fees.receipt_no + "-" + ai_fees.received_from.name, "debit":ai_fees.amount, "credit":None}
            statements.append(statement)
        for ei_fees in ei_fees_list:
            closing_balance += ei_fees.amount
            statement = {"date": ei_fees.date, "account_head": "Employee Internship Fees","description": ei_fees.receipt_no + "-" + ei_fees.received_from.name, "debit":ei_fees.amount, "credit":None}
            statements.append(statement)
        for cw_fees in cw_fees_list:
            closing_balance += cw_fees.amount
            statement = {"date": cw_fees.date, "account_head": "Cognitve Workshop Fees","description": cw_fees.receipt_no + "-" + cw_fees.received_from.name, "debit":cw_fees.amount, "credit":None}
            statements.append(statement)
        for aw_fees in aw_fees_list:
            closing_balance += aw_fees.amount
            statement = {"date": aw_fees.date, "account_head": "Academic Workshop Fees","description": aw_fees.receipt_no + "-" + aw_fees.received_from.name, "debit":aw_fees.amount, "credit":None}
            statements.append(statement)
        for sp_fees in sp_fees_list:
            closing_balance += sp_fees.amount
            statement = {"date": sp_fees.date, "account_head": "Student Project Fees","description": sp_fees.receipt_no + "-" + sp_fees.received_from.name, "debit":sp_fees.amount, "credit":None}
            statements.append(statement)


        statements = sorted(statements, key = lambda statement: (statement['date'], statement['description']))
        data = {"from_date": from_date, "to_date": to_date, "opening_balance": opening_balance, "closing_balance": closing_balance, "statements": statements}

        return Response(data)