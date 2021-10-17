"""alchemy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.main.views import start_main
from apps.subjects.views import SubjectList,professor_or_student_or_admin,SubjectCreate,SubjectDelete,SubjectUpdate
from apps.students.views import StudentCreate, StudentDelete,StudentList
from django.contrib.auth.views import LoginView,LogoutView
from apps.professors.views import ProfessorCreate,ProfessorList,ProfessorDelete
from apps.admins.views import AdminCreate,AdminList,AdminDelete,list
from apps.users.views import UserUpdate
from apps.imparts.views import create_imparts,delete_imparts
from apps.study.views import subject_student,enroll
from apps.basic_elements.views import BasicElementCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',start_main,name='index'),
    path('subjects/',SubjectList.as_view(),name='subjects'),
    path('subjects/<int:pk>',professor_or_student_or_admin,name='select'),
    path('subjects/create_subject',SubjectCreate.as_view(),name='create_subject'),
    path('subjects/edit_subject/<int:pk>',SubjectUpdate.as_view(),name='edit_subject'),
    path('subjects/delete_subject/<int:pk>',SubjectDelete.as_view(),name='delete_subject'),
    path('students/',StudentList.as_view(),name='students'),
    path('register_student/',StudentCreate.as_view(),name='register_student'),
    path('delete_student/<int:pk>',StudentDelete.as_view(),name='delete_student'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('professors/',ProfessorList.as_view(),name='professors'),
    path('professors/register_professor/',ProfessorCreate.as_view(),name='register_professor'),
    path('professors/delete_professor/<int:pk>',ProfessorDelete.as_view(),name='delete_professor'),
    path('admins/',AdminList.as_view(),name='admins'),
    path('admins/register_admin/',AdminCreate.as_view(),name='register_admin'),
    path('admins/delete_admin/<int:pk>',AdminDelete.as_view(),name='delete_admin'),
    path('edit_user/<int:pk>',UserUpdate.as_view(),name='edit_user'),
    path('subjects/subject_admin/<int:pk>',list,name='subject_admin'),
    path('subjects/subject_admin/create_imparts/<int:pk>',create_imparts,name='create_imparts'),
    path('subjects/subject_admin/delete_imparts/<str:pk>',delete_imparts,name='delete_imparts'),
    path('subjects/subject_student/<int:pk>',subject_student,name='subject_student'),
    path('subjects/subject_student/enroll/<int:pk>',enroll,name='enroll'),
    #path('subject/aubject_professor/<int:pk>',name='subject_professor'),
    path('subjects/subject_professor/create_basic_element/<int:pk>',BasicElementCreate.as_view(),'create_basic_element'),
]
