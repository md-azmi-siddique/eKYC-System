from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from ekyc import views
from django.contrib.auth import views as auth_views
from ekyc.models import Customer
from forms import LoginForm
from .router import router 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Dashboard, name='dashboard'),
    path('api/',include(router.urls)),
    
    path('account/login/', auth_views.LoginView.as_view(template_name='admin_login.html', authentication_form=LoginForm), name="login"),
    path('account/logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    
    path('dashboard/',views.Dashboard,name='dashboard'),
    
    path('addstudent/',views.AddStudent,name='addstudent'),
    path('viewstudent/',views.ViewStudent,name='viewstudent'),
    path('updatestudent/<str:pk>/',views.UpdateStudent,name='updatestudent'),
    path('deletestudent/<str:pk>/',views.DeleteStudent,name='deletestudent'),
    path('st_details/<str:pk>/',views.StudentDetails,name='st_details'),
    
    path('addcourse/',views.AddCourse,name='addcourse'),
    path('viewcourse/',views.ViewCourse,name='viewcourse'),
    path('updatecourse/<str:pk>/',views.UpdateCourse,name='updatecourse'),
    path('deletecourse/<str:pk>/',views.DeleteCourse,name='deletecourse'),
    
    path('addcustomer/',views.AddCustomer,name='addcustomer'),
    path('viewcustomer/',views.ViewCustomer,name='viewcustomer'),
    path('updatecustomer/<str:pk>/',views.UpdateCustomer,name='updatecustomer'),
    path('deletecustomer/<str:pk>/',views.DeleteCustomer,name='deletecustomer'),
    
    path('userpage/',views.Userpage, name='userpage')  
]

