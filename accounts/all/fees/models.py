from django.db import models
from django.utils import tree
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from administration.cognitive_solutions.programs.models import CognitiveInternship, AcademicInternship, EmployeeInternship, AcademicWorkshop, CognitiveWorkshop
from administration.codelab_systems.student_projects.models import StudentProject 
from django.db.models.signals import pre_save, post_save, post_delete
import datetime
from django.core.validators import MinValueValidator
# Create your models here.

class PaymentType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Fees(models.Model):
    #purpose option
    # REGISTRATION = 1
    # INTERNSHIP = 2
    # PURPOSE_CHOICES = (
    #     (REGISTRATION, 'REGISTRATION'),
    #     (INTERNSHIP, 'INTERNSHIP'),
    # )

    receipt_no = models.CharField(max_length=10, unique=True, editable=False,)
    date = models.DateField(auto_now_add=True)
    # recieved_from = models.ForeignKey()
    mode_of_payment = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True)
    # purpose = models.PositiveSmallIntegerField(choices=PURPOSE_CHOICES)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    # amount_in_words = models.TextField()

    class Meta:
        abstract = True

class InternshipFeesCleanMixin:
    def clean(self):
        """
        Check wether total fee is less than or equal to actual internship fees.
        """
        if not self.received_from:
            raise ValidationError(
            _('received_from field should not be null while creating or updating.'),
            code='empty_batch_field',
            )   

        if not self.received_from.batch:
            raise ValidationError(
            _('batch field is empty in registration form of %(received_from)s. cannot create or update fees.'),
            code='empty_batch_field',
            params={'received_from': self.received_from.register_no}
            )   

        if not self.received_from.batch.internship:
            raise ValidationError(
            _('internship field is empty in batch %(batch)s. cannot create or update fees.'),
            code='empty_internship_field',
            params={'batch': self.received_from.batch.name}
            )   

        internship_fees = self.received_from.batch.internship.actual_fees - self.received_from.concession
        # all_receipt = CognitiveInternshipFees.objects.filter(received_from=self.received_from)
        all_receipt = self._meta.model.objects.filter(received_from=self.received_from)
        paid_amount = 0
        now_paying = self.amount
        for receipt in all_receipt:
            if receipt.id != self.id:
                paid_amount += receipt.amount
        if paid_amount + now_paying > internship_fees:
            raise ValidationError(
            _('Total fees amount(%(fees_amount)s) exceed the actual fees with concession(%(actual_fees)s)'),
            code='invalid_fees_amount',
            params={'fees_amount': paid_amount+now_paying, 'actual_fees': internship_fees}
            )   

class CognitiveInternshipFees(InternshipFeesCleanMixin, Fees):
    received_from = models.ForeignKey(CognitiveInternship, on_delete=models.SET_NULL, null=True, related_name='ci_fees') 

    def __str__(self):
        return self.receipt_no + ':' + self.received_from.name

class AcademicInternshipFees(InternshipFeesCleanMixin, Fees):
    received_from = models.ForeignKey(AcademicInternship, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return self.receipt_no + ':' + self.received_from.name

class EmployeeInternshipFees(InternshipFeesCleanMixin, Fees):
    received_from = models.ForeignKey(EmployeeInternship, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return self.receipt_no + ':' + self.received_from.name

class WorkshopFeesCleanMixin:
    def clean(self):
        """
        Check wether total fee is less than or equal to actual internship fees.
        """
        if not self.received_from:
            raise ValidationError(
            _('received_from field should not be null while creating or updating.'),
            code='empty_received_from_field',
            )   

        if not self.received_from.workshop:
            raise ValidationError(
            _('workshop is empty in registration form of %(received_from)s. cannot create or update fees.'),
            code='empty_workshop_field',
            params={'received_from': self.received_from.register_no}
            )   

        workshop_fees = self.received_from.workshop.actual_fees - self.received_from.concession
        # all_receipt = CognitiveInternshipFees.objects.filter(received_from=self.received_from)
        all_receipt = self._meta.model.objects.filter(received_from=self.received_from)
        paid_amount = 0
        now_paying = self.amount
        for receipt in all_receipt:
            if receipt.id != self.id:
                paid_amount += receipt.amount
        if not paid_amount + now_paying == workshop_fees:
            raise ValidationError(
            _('''Total fees amount(%(fees_amount)s) must be equal to actual fees with concession(%(actual_fees)s)
            or actual fees with concession(%(actual_fees)s) must be paid in one installment.'''),
            code='invalid_fees_amount',
            params={'fees_amount': paid_amount+now_paying, 'actual_fees': workshop_fees}
            )   
 
class CognitiveWorkshopFees(WorkshopFeesCleanMixin, Fees):
    received_from = models.OneToOneField(CognitiveWorkshop, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return self.receipt_no + ':' + self.received_from.name

class AcademicWorkshopFees(WorkshopFeesCleanMixin, Fees):
    received_from = models.OneToOneField(AcademicWorkshop, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return self.receipt_no + ':' + self.received_from.name

class StudentProjectFeesCleanMixin:
    def clean(self):
        """
        Check wether total fee is less than or equal to actual internship fees.
        """
        if not self.received_from:
            raise ValidationError(
            _('received_from field  cannot be null while creating or updating.'),
            code='empty_received_from_field',
            )   

        # if not self.received_from.project:
        #     raise ValidationError(
        #     _('project is empty in registration form of %(received_from)s. cannot create or update fees.'),
        #     code='empty_workshop_field',
        #     params={'received_from': self.received_from.register_no}
        #     )   

        student_project_fees = self.received_from.actual_fees - self.received_from.concession
        # all_receipt = CognitiveInternshipFees.objects.filter(received_from=self.received_from)
        all_receipt = self._meta.model.objects.filter(received_from=self.received_from)
        paid_amount = 0
        now_paying = self.amount
        for receipt in all_receipt:
            if receipt.id != self.id:
                paid_amount += receipt.amount
        # print('clean', paid_amount - self.amount)
        if paid_amount + now_paying > student_project_fees:
            raise ValidationError(
            _('Total fees amount(%(fees_amount)s) exceed the actual fees (%(actual_fees)s)'),
            code='invalid_fees_amount',
            params={'fees_amount': paid_amount+now_paying, 'actual_fees': student_project_fees}
            )   

class StudentProjectFees(StudentProjectFeesCleanMixin, Fees):
    received_from = models.ForeignKey(StudentProject, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return self.receipt_no + ':' + self.received_from.name

    @property
    def paid_amount(self):
        all_receipt = self._meta.model.objects.filter(received_from=self.received_from)
        paid_amount = 0
        for receipt in all_receipt:
            paid_amount += receipt.amount
        # print('paid_amount', paid_amount)
        return paid_amount 

    @property
    def balance(self):
        all_receipt = self._meta.model.objects.filter(received_from=self.received_from)
        paid_amount = self.paid_amount 
        balance = self.received_from.fees - paid_amount
        return balance
    

def get_prefix(argument): 
    switcher = { 
        CognitiveInternshipFees: "CIF", 
        AcademicInternshipFees: "AIF", 
        EmployeeInternshipFees: "EIF", 
        CognitiveWorkshopFees: "CWF", 
        AcademicWorkshopFees: "AWF",
        StudentProjectFees:"SPF" 
    } 
  
    return switcher.get(argument, "SHAF")

def set_receipt_no(sender, instance, **kwargs):
    if instance._state.adding:
        try:
            latest_id = int(sender.objects.latest('id').receipt_no[-3:])
        except sender.DoesNotExist:
            latest_id = 0
        year = str(datetime.datetime.now().year)[-2:]
        instance.receipt_no = get_prefix(sender) + year + '-' + "{:03d}".format(latest_id + 1)

def set_internship_is_fees_paid(sender, instance, **kwargs):
    if not instance.received_from:
        return 
    elif not instance.received_from.batch or not instance.received_from.batch.internship:
        instance.received_from.is_fees_paid = False 
        instance.received_from.save()
        return

    if instance.received_from.is_fees_paid == True:
        instance.received_from.is_fees_paid = False 
    all_receipt = sender.objects.filter(received_from=instance.received_from)
    amount = 0
    for receipt in all_receipt:
        amount += receipt.amount
    if amount == instance.received_from.batch.internship.actual_fees - instance.received_from.concession:
        instance.received_from.is_fees_paid = True

    instance.received_from.save()

def set_workshop_is_fees_paid(sender, instance, **kwargs):
    if not instance.received_from:
        return 
    elif not instance.received_from.workshop:
        instance.received_from.is_fees_paid = False 
        instance.received_from.save()
        return

    if instance.received_from.is_fees_paid == True:
        instance.received_from.is_fees_paid = False 
    all_receipt = sender.objects.filter(received_from=instance.received_from)
    amount = 0
    for receipt in all_receipt:
        amount += receipt.amount
    if amount == instance.received_from.workshop.actual_fees - instance.received_from.concession:
        instance.received_from.is_fees_paid = True

    instance.received_from.save()

def set_student_project_is_fees_paid(sender, instance, **kwargs):
    if not instance.received_from:
        return 
    elif not instance.received_from.project:
        instance.received_from.is_fees_paid = False 
        instance.received_from.save()
        return

    if instance.received_from.is_fees_paid == True:
        instance.received_from.is_fees_paid = False 
    all_receipt = sender.objects.filter(received_from=instance.received_from)
    amount = 0
    for receipt in all_receipt:
        amount += receipt.amount
    if amount == instance.received_from.actual_fees - instance.received_from.concession:
        instance.received_from.is_fees_paid = True

    instance.received_from.save()

pre_save.connect(set_receipt_no, sender=CognitiveInternshipFees)
pre_save.connect(set_receipt_no, sender=AcademicInternshipFees)
pre_save.connect(set_receipt_no, sender=EmployeeInternshipFees)
pre_save.connect(set_receipt_no, sender=CognitiveWorkshopFees)
pre_save.connect(set_receipt_no, sender=AcademicWorkshopFees)
pre_save.connect(set_receipt_no, sender=StudentProjectFees)

post_save.connect(set_internship_is_fees_paid, sender=CognitiveInternshipFees)
post_save.connect(set_internship_is_fees_paid, sender=AcademicInternshipFees)
post_save.connect(set_internship_is_fees_paid, sender=EmployeeInternshipFees)
post_save.connect(set_workshop_is_fees_paid, sender=AcademicWorkshopFees)
post_save.connect(set_workshop_is_fees_paid, sender=CognitiveWorkshopFees)
post_save.connect(set_student_project_is_fees_paid, sender=StudentProjectFees)

post_delete.connect(set_internship_is_fees_paid, sender=CognitiveInternshipFees)
post_delete.connect(set_internship_is_fees_paid, sender=AcademicInternshipFees)
post_delete.connect(set_internship_is_fees_paid, sender=EmployeeInternshipFees)
post_delete.connect(set_workshop_is_fees_paid, sender=AcademicWorkshopFees)
post_delete.connect(set_workshop_is_fees_paid, sender=CognitiveWorkshopFees)
post_delete.connect(set_student_project_is_fees_paid, sender=StudentProjectFees)