#from .View.Others import IndexView, Department, Academy, User, SuperAdminstration, AcademicAdminstration, CaptchaStore, Counsellor, Teacher, Student, refresh_captcha
from django.contrib import admin
from django.urls import path
#from .import AttendanceInformation, AttendanceInformationClass, CourseInformation, CourseArrangement, EquipmentInformation, IDEvaluation, Login, Logout, PersonInformation, StudentAttendance, StudentsInformation, TeachersInformation

from .Views.AttendanceInformation import AttendanceInformation
from .Views.AttendanceInformationClass import AttendanceInformationClass
from .Views.CourseInformation import CourseInformation
from .Views.CourseArrangement import CourseArrangement
from .Views.EquipmentInformation import EquipmentInformation
from .Views.IDEvaluation import IDEvaluation
from .Views.Login import Login
from .Views.Logout import Logout
from .Views.PersonInformation import PersonInformation
from .Views.StudentAttendance import StudentAttendance
from .Views.StudentsInformation import StudentsInformation
from .Views.TeachersInformation import TeachersInformation
from .Views.UserInformation import UserInformation
from .Views.Picture import Picture
from .Views.QuitWarning import QuitWarning
from .Views.StudentView import student_login, student_index, student_changepsw, student_lessons, student_changepswsuccess, student_attendtime, student_lessoninfo, student_statistics
app_name = 'polls'
urlpatterns = [
    path('Logout/', Logout.as_view(), name='Logout'),
    path('Login/', Login.as_view(), name='Login'),
    path('PersonInformation/',
         PersonInformation.as_view(),
         name='PersonInformation'),
    path('IDEvaluation/', IDEvaluation.as_view(), name='IDEvaluation'),
    path('EquipmentInformation/',
         EquipmentInformation.as_view(),
         name='EquipmentInformation'),
    path('StudentsInformation/',
         StudentsInformation.as_view(),
         name='StudentsInformation'),
    path('TeachersInformation/',
         TeachersInformation.as_view(),
         name='TeachersInformation'),
    path('CourseInformation/',
         CourseInformation.as_view(),
         name='CourseInformation'),
    path('AttendanceInformation/',
         AttendanceInformation.as_view(),
         name='AttendanceInformation'),
    path('AttendanceInformationClass/',
         AttendanceInformationClass.as_view(),
         name='AttendanceInformationClass'),
    path('StudentAttendance/',
         StudentAttendance.as_view(),
         name='StudentAttendance'),
    path('CourseArrangement/',
         CourseArrangement.as_view(),
         name='CourseArrangement'),
    path('QuitWarning/', QuitWarning.as_view(), name='QuitWarning'),
    #path('UserInformation/',UserInformation.as_view(), name='UserInformation'),
    path('Picture/', Picture.as_view(), name='Picture'),
    path('student/login/', student_login, name='student_login'),
    path('student/index/', student_index, name='student_index'),
    path('student/changepswsuccess/', student_changepswsuccess,
         name='student_changepswsuccess'),
    path('student/changepsw/', student_changepsw, name='student_changepsw'),
    path('student/lessons/', student_lessons, name="student_lessons"),
    path('student/statistics/<int:id>',
         student_attendtime, name="student_attendtime"),
    path('student/lessoninfo/<int:id>',
         student_lessoninfo, name="student_lessoninfo"),
    path('student/lessons/lessoninfo/<int:id>',
         student_lessoninfo, name="student_lessoninfo"),
    path('student/index/lessoninfo/<int:id>',
         student_lessoninfo, name="student_lessoninfo"),
    path('student/statistics/', student_statistics,
         name="student_statistics"),
    # path('IndexView',IndexView.as_view(),name='IndexView'),
    #path('department/', Department.as_view(), name='department'),
    #path('academy/', Academy.as_view(), name='academy'),
    #path('user/', User.as_view(), name='user'),
    #path('refresh_captcha/', refresh_captcha),
    # path('SuperAdministration/',SuperAdminstration.as_view(),name='SuperAdministration'),
    # path('AcademicAdministration/',AcademicAdminstration.as_view(),name='AcademicAdministration'),
    #path('Counsellor/', Counsellor.as_view(), name='Counsellor'),
    #path('Teacher/', Teacher.as_view(), name='Teacher'),
    #path('Student/', Student.as_view(), name='Student'),
]
