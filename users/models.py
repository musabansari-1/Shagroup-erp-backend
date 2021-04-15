from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.core.validators import MinValueValidator

class User(AbstractUser):
    #Other
    OTHER = 0
    #Departments
    ADMINISTRATION = 1
    ACCOUNTS = 2
    DEPARTMENT_CHOICES = (
        (OTHER, 'Other'),
        (ADMINISTRATION, 'Administration'),
        (ACCOUNTS, 'Accounts'),
    )
    #Roles
    ROLE_CHOICES = (
        (OTHER, 'Other'),
    ) 
    #Other Detail
    username = None
    email = models.EmailField(unique=True)
    department = models.PositiveSmallIntegerField(choices=DEPARTMENT_CHOICES, default=OTHER, validators=[MinValueValidator(0)])
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=OTHER, validators=[MinValueValidator(0)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['department', 'role',]

    objects = CustomUserManager()


    # def __str__(self):
    #     return self.first_name 

