from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ekyc.models import Course, Student, Customer
from .forms import StudentForm
from .forms import CourseForm
from .forms import CustomerForm
import requests

# Create your views here.
@login_required(login_url="/account/login/")

def Userpage(request):
    return render(request, 'user.html')

def Dashboard(request):
    return render(request,'admin_home.html')

def AddStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewstudent')
    context = {'form':form}
    return render(request,'add_student.html', context)


def ViewStudent(request):
    student = Student.objects.all()
    return render(request,'student_info.html', {'student':student})

def UpdateStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('viewstudent')
    context = {'form':form}
    return render(request,'add_student.html', context)

def DeleteStudent(request, pk):
    emp = Student.objects.filter(id =pk)
    emp.delete()
    context = {
        'emp':emp,
    }
    return redirect('viewstudent')
    
def StudentDetails(requset, pk):
    student = Student.objects.get(id=pk)
    context = {'student':student}
    return render(requset, 'st_details.html', context)

def GradeStudent(requset, pk):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewstudent')
    context = {'form':form}
    return render(request,'add_student.html', context)

    
     

#COURSE
def AddCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewcourse')
    context = {'form':form}
    return render(request,'add_course.html', context)

def ViewCourse(request):
    course = Course.objects.all()
    return render(request,'course_info.html', {'course':course})

def UpdateCourse(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('viewcourse')
    context = {'form':form}
    return render(request,'add_course.html', context)

def DeleteCourse(request, pk):
    emp = Course.objects.filter(id =pk)
    emp.delete()
    context = {
        'emp':emp,
    }
    return redirect('viewcourse')


    

#customer
def AddCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewcustomer')
    context = {'form':form}
    return render(request,'add_customer.html', context)

def ViewCustomer(request):
    customer = Customer.objects.all()
    return render(request,'customer_info.html', {'customer':customer})

def UpdateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('viewcustomer')
    context = {'form':form}
    return render(request,'add_customer.html', context)

def DeleteCustomer(request, pk):
    emp = Customer.objects.filter(id =pk)
    emp.delete()
    context = {
        'emp':emp,
    }
    return redirect('viewcustomer')


