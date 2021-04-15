from enum import unique
from django.db import models
from django.db.models.signals import pre_save
from administration.cognitive_solutions.programs.models import Course, PersonalDetail as PD, Frontend, Backend, College, Company, Stream, set_image_and_register_no
from django.core.validators import MinLengthValidator,validate_integer,int_list_validator, MinValueValidator
from utils.utils import validate_date_range

# Create your models here.
class PersonalDetail(PD):
    is_whatsapp_contact_1 = models.BooleanField(default=False)
    is_whatsapp_contact_2 = models.BooleanField(default=False)

    class Meta:
        abstract = True



class PresentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    stream = models.ForeignKey(Stream, on_delete=models.SET_NULL, null=True)
    college = models.ForeignKey(College, models.SET_NULL, null=True)
    college_register_no = models.CharField(max_length=20)

    class Meta:
        abstract = True

class Trainer(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class TrainerRole(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    client_name = models.CharField(max_length=40)
    client_contact = models.CharField(max_length=10, validators=[int_list_validator(sep='',), MinLengthValidator(10), ])
    client_email = models.EmailField()
    frontend = models.ForeignKey(Frontend, on_delete=models.SET_NULL, null=True) 
    backend = models.ForeignKey(Backend, on_delete=models.SET_NULL, null=True) 
    trainer_1_name = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    trainer_1_role = models.ForeignKey(TrainerRole, on_delete=models.SET_NULL, null=True)
    trainer_2_name = models.ForeignKey(Trainer, related_name='trainer_2', on_delete=models.SET_NULL, null=True)
    trainer_2_role = models.ForeignKey(TrainerRole, related_name='trainer_2_role', on_delete=models.SET_NULL, null=True)
    # actual_fees = models.FloatField(validators=[MinValueValidator(0)])
    from_date = models.DateField()
    to_date = models.DateField()
    
    def __str__(self):
        return self.title

    def clean(self):
        validate_date_range(from_date=self.from_date, to_date=self.to_date)   

# class ScheduleDetail(models.Model):
#     from_date = models.DateField()
#     to_date = models.DateField()

#     class Meta:
#         abstract = True

class SSLC(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class PUC(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class AcademicDetail(models.Model):
    sslc = models.ForeignKey(SSLC, on_delete=models.SET_NULL, null=True)
    sslc_percentage = models.FloatField(validators=[MinValueValidator(0)])
    sslc_no_of_attempts = models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(0)])
    puc = models.ForeignKey(PUC, on_delete=models.SET_NULL, null=True)
    puc_percentage = models.FloatField(validators=[MinValueValidator(0)])
    puc_no_of_attemps = models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(0)])
    degree = models.ForeignKey(College, related_name='degree', on_delete=models.SET_NULL, null=True)
    degree_percentage = models.FloatField(validators=[MinValueValidator(0)])
    degree_no_of_attempts = models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(0)])
    additional_qualifications = models.TextField()
    extracurricular_activities = models.TextField()
    
    class Meta:
        abstract = True 

class StudentProject(PersonalDetail, PresentCourse, AcademicDetail):
    register_no = models.CharField(max_length=8, unique=True, editable=False,)
    is_fees_paid = models.BooleanField(default=False, editable=False)
    actual_fees = models.FloatField(validators=[MinValueValidator(0)])
    concession = models.FloatField(validators=[MinValueValidator(0)])
    # fees = models.FloatField(validators=[MinValueValidator(0)])
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
   
    def __str__(self):
        return self.register_no + ':' + self.name

pre_save.connect(set_image_and_register_no, sender=StudentProject)