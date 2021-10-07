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
from apps.subjects.views import SubjectList,professor_or_student,SubjectCreate,SubjectDelete,SubjectUpdate
from apps.students.views import StudentCreate, StudentDelete,StudentList
from django.contrib.auth.views import LoginView,LogoutView
from apps.professors.views import ProfessorCreate,ProfessorList,ProfessorDelete
from apps.admins.views import AdminCreate,AdminList,AdminDelete
from apps.users.views import UserUpdate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',start_main,name='index'),
    path('subjects/',SubjectList.as_view(),name='subjects'),
    path('subjects/<int:pk>',professor_or_student,name='select'),
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
    path('edit_user/<int:pk>',UserUpdate.as_view(),name='edit_user')
]
