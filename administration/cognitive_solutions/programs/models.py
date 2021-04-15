from django.db import models
from django.db.models import base
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.core.validators import MinLengthValidator,validate_integer,int_list_validator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from utils.utils import validate_date_range

class PersonalDetail(models.Model):
    name = models.CharField(max_length=40)
    profile_pic = models.ImageField(upload_to='profile_pic/', default='profile_pic/default.png' ,null=True, ) 
    address = models.TextField()
    contact_1 = models.CharField(max_length=10, validators=[int_list_validator(sep='',), MinLengthValidator(10), ])
    contact_2 = models.CharField(max_length=10, null=True, blank=True, validators=[int_list_validator(sep='',), MinLengthValidator(10), ])
    email = models.EmailField(null=True, blank=True)
    guardian_name = models.CharField(max_length=40,)
    guardian_contact = models.CharField(max_length=10, validators=[int_list_validator(sep='',), MinLengthValidator(10), ])

    class Meta:
        abstract = True

class College(models.Model):
    name = models.CharField(max_length=40, unique=True)
    place = models.CharField(max_length=30)
    district = models.CharField(max_length=30) 
    state = models.CharField(max_length=30) 

    def __str__(self):
        return self.name + '-' + self.place

class Course(models.Model):
    name = models.CharField(max_length=40, unique=True)
    max_sem = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    
    def __str__(self):
        return self.name + '-' + str(self.max_sem) + ' sem'

class Stream(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20)

    class Meta:
        # unique_together = ('course', 'name',)
            
        constraints = [
            models.UniqueConstraint(fields=['course', 'name'], name='limit_course')
        ]

    def __str__(self):
        return self.name

class Student(PersonalDetail):
    #academic details
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    semester = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        abstract = True

    def clean(self):
        try:
            if not self.course:
                raise ValidationError(
            _('course field should not be null while creating or updating.'),
            code='empty_course_field',
            )   
            
            if not (self.semester > 0 and self.semester <= self.course.max_sem):
                raise ValidationError(
            _('semester value must be between 1 and %(max_sem)s for course %(course)s'),
            code='invalid_semester_value',
            params={'max_sem': self.course.max_sem, 'course': self.course.name}
            )   
        except (self._meta.model.course.RelatedObjectDoesNotExist, TypeError):
            raise ValidationError(
        _('Course must be selected to enter semester'),
        code='invalid_semested_value',
        )


class Company(models.Model):
    name = models.CharField(max_length=40, unique=True)
    place = models.CharField(max_length=20)
    website = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name

class Employee(PersonalDetail):
    #employement detail
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=20)

    class Meta:
        abstract = True

class Frontend(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Backend(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Internship(models.Model):
    name = models.CharField(max_length=25)
    no_of_months = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    frontend = models.ForeignKey(Frontend, on_delete=models.SET_NULL, null=True)
    backend = models.ForeignKey(Backend, on_delete=models.SET_NULL, null=True)
    actual_fees = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name



class Batch(models.Model):
    ONGOING = 1
    CLOSED = 0
    STATUS_CHOICES = (
        (ONGOING, 'Ongoing'),
        (CLOSED, 'Closed'),
    )
    name = models.CharField(max_length=40)
    internship = models.ForeignKey(Internship, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField(editable=False, null=True, blank=False)
    from_time = models.TimeField()
    to_time = models.TimeField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=ONGOING, validators=[MinValueValidator(0)],)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.status == Batch.CLOSED:
            self.end_date = datetime.date.today()
        super(Batch, self).save(*args, **kwargs)

    # def clean(self):
    #     validate_date_range(from_date=self.start_date, to_date=self.end_date)

class CommonField(models.Model):
    register_no = models.CharField(max_length=8, unique=True, editable=False,)
    
    #internship details
    # start_date = models.DateField()
    # end_date = models.DateField()
    # from_time = models.TimeField()
    # to_time = models.TimeField()
    # frontend = models.ForeignKey(Frontend, on_delete=models.CASCADE, null=False, blank=False)
    # backend = models.ForeignKey(Backend, on_delete=models.CASCADE, null=False, blank=False)

    #fees details
    is_fees_paid = models.BooleanField(default=False, editable=False)
    concession = models.FloatField(validators=[MinValueValidator(0)])
    # actual_fees = models.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        abstract = True

class InternshipCommonField(CommonField):
    date_of_admission = models.DateField(auto_now_add=True)
    # internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

class Workshop(models.Model):
    name = models.CharField(max_length=40)
    date_of_workshop = models.DateField()
    no_of_days = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    no_of_hours = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    start_date = models.DateField()
    end_date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    technology = models.TextField()
    actual_fees = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name 

    def clean(self):
        validate_date_range(from_date=self.start_date, to_date=self.end_date)

class WorkshopCommonField(Student, CommonField):
    guardian_name = None
    guardian_contact = None
    workshop = models.ForeignKey(Workshop, on_delete=models.SET_NULL, null=True)
    # date_of_workshop = models.DateField()
    # no_of_days = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    # no_of_hours = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    # frontend = models.ForeignKey(Frontend, on_delete=models.CASCADE, null=False, blank=False)
    # backend = models.ForeignKey(Backend, on_delete=models.CASCADE, null=False, blank=False)
    # actual_fees = models.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        abstract = True

class AcademicInternship(Student, InternshipCommonField):
    overall_percentage = models.FloatField(validators=[MinValueValidator(0)])
    backlog = models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(0)])
 
    def __str__(self):
        return self.register_no + ':' +self.name


class CognitiveInternship(Student, InternshipCommonField):
    # no_of_months = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    course = None
    semester = None
    previous_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.register_no + ':' +self.name

    def clean(self):
        pass

class EmployeeInternship(Employee, InternshipCommonField):
    # no_of_months = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    def __str__(self):
        return self.register_no + ':' +self.name

class AcademicWorkshop(WorkshopCommonField):
    def __str__(self):
        return self.register_no + ':' +self.name

class CognitiveWorkshop(WorkshopCommonField):
    def __str__(self):
        return self.register_no + ':' +self.name

def get_prefix(argument): 
    switcher = { 
        CognitiveInternship: "CI", 
        AcademicInternship: "AI", 
        EmployeeInternship: "EI", 
        CognitiveWorkshop: "CW", 
        AcademicWorkshop: "AW", 
    } 
  
    return switcher.get(argument, "SP") #default is SP because it is used in StudentProject Model to create register no.

def set_image_and_register_no(sender, instance, **kwargs):
    if not instance._state.adding:
        if not instance.profile_pic:
            obj = sender.objects.get(id=instance.id)
            if not obj.profile_pic:
                instance.profile_pic = 'profile_pic/default.png'
            else:
                instance.profile_pic = obj.profile_pic
    else:
        try:
            latest_id = int(sender.objects.latest('id').register_no[-3:])
        except sender.DoesNotExist:
            latest_id = 0
        year = str(datetime.datetime.now().year)[-2:]
        instance.register_no = get_prefix(sender) + year + '-' + "{:03d}".format(latest_id + 1)
    
        if not instance.profile_pic:
            instance.profile_pic = 'profile_pic/default.png'

# def update_fees(sender, instance, **kwargs):
#     if not instance._state.adding:
#         ci = CognitiveInternship.objects.filter(batch__internship__id = instance.id)
#         print(len(ci))

pre_save.connect(set_image_and_register_no, sender=CognitiveInternship)
pre_save.connect(set_image_and_register_no, sender=AcademicInternship)
pre_save.connect(set_image_and_register_no, sender=EmployeeInternship)
pre_save.connect(set_image_and_register_no, sender=CognitiveWorkshop)
pre_save.connect(set_image_and_register_no, sender=AcademicWorkshop)

# post_save.connect(update_fees, sender=Internship)
# @receiver(pre_save, sender=CognitiveInternship)
# def set_uninitialized_values(sender, instance, **kwagrs):
#     set_image_and_register_no(sender, instance) 

