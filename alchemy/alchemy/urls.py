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
from apps.imparts.views import create_imparts,delete_imparts,request_list
from apps.study.views import subject_student,enroll,delete_study
from apps.basic_elements.views import BasicElementCreate,basic_element_list,make_visible,BasicElementEdit,delete_basic_element
from apps.non_basic_elements.views import accepted_list, create_non_basic_element,pending_list,delete_non_basic_element,accept_non_basic_element,reject_non_basic_element

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
    path('subjects/subject_admin/delete_imparts/<int:pk>',delete_imparts,name='delete_imparts'),
    path('subjects/subject_admin/delete_study/<int:pk>',delete_study,name='delete_study'),
    path('subjects/subject_student/<int:pk>',subject_student,name='subject_student'),
    path('subjects/subject_student/enroll/<int:pk>',enroll,name='enroll'),
    path('subject/subject_professor/<int:pk>',request_list,name='subject_professor'),
    path('subject/subject_professor/basic_elements/<int:pk>',basic_element_list,name='basic_elements'),
    path('subjects/subject_professor/basic_elements/create_basic_element/<int:pk>',BasicElementCreate.as_view(),name='create_basic_element'),
    path('subjects/subject_professor/basic_elements/make_visible/<int:pk>',make_visible,name='make_visible'),
    path('subjects/subject_professor/basic_elements/edit_basic_element/<int:pk>',BasicElementEdit.as_view(),name='edit_basic_element'),
    path('subjects/subject_professor/basic_element/delete_basic_element/<int:pk>',delete_basic_element,name='delete_basic_element'),
    path('subjects/subject_student/accepted_list/<int:pk>',accepted_list,name='accepted_list'),
    path('subjects/subject_student/pending_list/<int:pk>',pending_list,name='pending_list'),
    path('subjects/subject_student/create_non_basic_element/<int:pk>',create_non_basic_element,name='create_non_basic_element'),
    path('subjects/subject_student/pending_list/delete_element/<int:pk>',delete_non_basic_element,name='delete_non_basic_element'),
    path('subjects/subject_professor/accept_element/<int:pk>',accept_non_basic_element,name="accept_element"),
    path('subjects/subject_professor/reject_element/<int:pk>',reject_non_basic_element,name="reject_element")
]
