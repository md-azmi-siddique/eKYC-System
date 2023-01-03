from django.forms import ModelForm, fields, widgets
from django import forms
from .models import Student
from .models import Course
from .models import Customer
from .models import Cgpa

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
        

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class GradeForm(ModelForm):
    class Meta:
        model = Cgpa
        fields = '__all__'

        

        