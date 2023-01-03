from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomerManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class Student(models.Model):
    STUDENT_TYPE = (
        ('Undergraduate', 'Undergraduate'),
        ('Graduate', 'Graduate'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    
    CITY = (
        ('Dhaka', 'Dhaka'),
        ('Chittagong', 'Chittagong'),
        ('Khulna', 'Khulna'),
        ('Rajshahi', 'Rajshahi'),
        ('Sylhet', 'Sylhet'),
        ('Mymensingh', 'Mymensingh'),
        ('Barisal', 'Barisal'),
        ('Rangpur', 'Rangpur'),
        ('Comilla', 'Comilla'),
        ('Narayanganj', 'Narayanganj'),
        ('Gazipur', 'Gazipur'),
    )
    
    BG = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    file = models.FileField(null = True)
    student_type = models.CharField(max_length=50, choices=STUDENT_TYPE, null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, choices=GENDER, null=True)
    nid = models.CharField(max_length=50, null=True)
    dob = models.CharField(max_length=50, null=True)
    present_address = models.CharField(max_length=50, null=True)
    permanent_address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, choices=CITY, null=True)
    zip = models.CharField(max_length=50, null=True)
    hight = models.CharField(max_length=50, null=True)
    weight = models.CharField(max_length=50, null=True)
    bg = models.CharField(max_length=50, null=True, choices=BG)
    medical_records = models.CharField(max_length=50, null=True)
    father_name = models.CharField(max_length=50, null=True)
    mother_name = models.CharField(max_length=50, null=True)
    father_contact = models.CharField(max_length=50, null=True)
    mother_contact = models.CharField(max_length=50, null=True)
    parents_address = models.CharField(max_length=50, null=True)
    parents_finantial_info = models.CharField(max_length=50, null=True)

    
    
    def __str__(self):
        return self.name


class Course(models.Model):
    
    CREDIT = (
        ('1', '1'),
        ('1.5', '1.5'),
        ('3', '3'),
    )
    code = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    credit = models.CharField(max_length=50, choices=CREDIT, null=True)
    
    def __str__(self):
        return self.code
    
    
class Semester(models.Model):
    
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name
    
    
class Grade(models.Model):
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name
    
        
class Cgpa(models.Model):
    name = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    code = models.ManyToManyField(Course)
    semester = models.ManyToManyField(Semester)
    grade = models.ManyToManyField(Grade)
    
class Customer(AbstractUser):
    username = None
    is_varified = models.BooleanField(default=False)
    bin= models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=50, null=True)
    file = models.FileField(null = True)

    
    objects = CustomerManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
@receiver(post_save,sender =settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)
    

    

    

