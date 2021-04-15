from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class AccountHead(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Expense(models.Model):
    GENERAL = 0
    COGNITIVE_SOLUTIONS = 1
    CODELAB_SYSTEMS = 2
    DATAQUE_SYSTEMS = 3
    DIVISION_CHOICES = (
        (GENERAL , 'GENERAL'),
        (COGNITIVE_SOLUTIONS, 'COGNITIVE SOLUTIONS'),
        (CODELAB_SYSTEMS, 'CODELAB SYSTEMS'),
        (DATAQUE_SYSTEMS , 'DATAQUE SYSTEMS'),
    )
    account_head = models.ForeignKey(AccountHead, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    paid_by = models.CharField(max_length=40)
    paid_to = models.CharField(max_length=40)
    paid_date = models.DateField()
    paid_amount = models.FloatField(validators=[MinValueValidator(0)])
    paid_status = models.BooleanField(default=False)
    division = models.PositiveSmallIntegerField(choices=DIVISION_CHOICES, default=GENERAL, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.account_head.name + "|" + self.description + "|" + self.paid_by