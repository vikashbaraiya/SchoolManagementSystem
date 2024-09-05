from django.urls import path
from account.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView
from .View.StudentView import StudentRegistrationView, StudentAddView, StudentRetrieveUpdateDeleteAPIView
from .View.CollegeView import CollegeAddView, CollegeRetrieveUpdateDeleteAPIView
from .View.CourseView import CourseAddView, CourseRetrieveUpdateDeleteAPIView
from .View.MarkSheetView import MarkSheetAddView, MarksheetRetrieveUpdateDeleteAPIView
from .View.SubjectView import SubjectAddView, SubjectRetrieveUpdateDeleteAPIView
from .View.FacultyView import FacultyAddView, FacultyRetrieveUpdateDeleteAPIView
from .View.TimeTableView import TimeTableAddView, TimeTableRetrieveUpdateDeleteAPIView
from .views import *


urlpatterns = [
    path('student_registration/', StudentRegistrationView.as_view(), name='student-registration'),

    path('college/', CollegeAddView.as_view(), name='college'),
    path('collegelist/', CollegeAddView.as_view(), name='college-list'),
    path('college/retreive/<int:pk>/', CollegeRetrieveUpdateDeleteAPIView.as_view(), name='college_retrive'),
    path('college/update/<int:pk>/', CollegeRetrieveUpdateDeleteAPIView.as_view(), name='college_update'),
    path('college/partial_update/<int:pk>/', CollegeRetrieveUpdateDeleteAPIView.as_view(), name='college_partial_update'),
    path('college/delete/<int:pk>/', CollegeRetrieveUpdateDeleteAPIView.as_view(), name='college_delete'), 

    path('course/', CourseAddView.as_view(), name='course'),
    path('courselist/', CourseAddView.as_view(), name='course-list'),
    path('course/retreive/<int:pk>/', CourseRetrieveUpdateDeleteAPIView.as_view(), name='course_retrive'),
    path('course/update/<int:pk>/', CourseRetrieveUpdateDeleteAPIView.as_view(), name='course_update'),
    path('course/partial_update/<int:pk>/', CourseRetrieveUpdateDeleteAPIView.as_view(), name='course_partial_update'),
    path('course/delete/<int:pk>/', CourseRetrieveUpdateDeleteAPIView.as_view(), name='course_delete'),   

    path('marksheet/', MarkSheetAddView.as_view(), name='marksheet'),
    path('marksheetlist/', MarkSheetAddView.as_view(), name='marksheet-list'),
    path('marksheet/retreive/<int:pk>/', MarksheetRetrieveUpdateDeleteAPIView.as_view(), name='marksheet_retrive'),
    path('marksheet/update/<int:pk>/', MarksheetRetrieveUpdateDeleteAPIView.as_view(), name='marksheet_update'),
    path('marksheet/partial_update/<int:pk>/', MarksheetRetrieveUpdateDeleteAPIView.as_view(), name='marksheet_partial_update'),
    path('marksheet/delete/<int:pk>/', MarksheetRetrieveUpdateDeleteAPIView.as_view(), name='marksheet_delete'),   
    
    path('student/', StudentAddView.as_view(), name='student_add'),
    path('studentlist/', StudentAddView.as_view(), name='student-list'),
    path('student/retreive/<int:pk>/', StudentRetrieveUpdateDeleteAPIView.as_view(), name='student_retrive'),
    path('student/update/<int:pk>/', StudentRetrieveUpdateDeleteAPIView.as_view(), name='student_update'),
    path('student/partial_update/<int:pk>/', StudentRetrieveUpdateDeleteAPIView.as_view(), name='student_partial_update'),
    path('student/delete/<int:pk>/', StudentRetrieveUpdateDeleteAPIView.as_view(), name='student_delete'), 

    path('subject/', SubjectAddView.as_view(), name='subject'),
    path('subjectlist/', SubjectAddView.as_view(), name='subject-list'),
    path('subject/retreive/<int:pk>/', SubjectRetrieveUpdateDeleteAPIView.as_view(), name='subject_retrive'),
    path('subject/update/<int:pk>/', SubjectRetrieveUpdateDeleteAPIView.as_view(), name='subject_update'),
    path('subject/partial_update/<int:pk>/', SubjectRetrieveUpdateDeleteAPIView.as_view(), name='subject_partial_update'),
    path('subject/delete/<int:pk>/', SubjectRetrieveUpdateDeleteAPIView.as_view(), name='subject_delete'),   
    
    path('faculty/',  FacultyAddView.as_view(), name='faculty'),
    path('facultylist/', FacultyAddView.as_view(), name='faculty-list'),
    path('faculty/retreive/<int:pk>/', FacultyRetrieveUpdateDeleteAPIView.as_view(), name='faculty_retrive'),
    path('faculty/update/<int:pk>/', FacultyRetrieveUpdateDeleteAPIView.as_view(), name='faculty_update'),
    path('faculty/partial_update/<int:pk>/', FacultyRetrieveUpdateDeleteAPIView.as_view(), name='faculty_partial_update'),
    path('faculty/delete/<int:pk>/', FacultyRetrieveUpdateDeleteAPIView.as_view(), name='faculty_delete'),   
    
    path('timetable/', TimeTableAddView.as_view(), name='timetable'),
    path('timetablelist/', TimeTableAddView.as_view(), name='timetable-list'),
    path('timetable/retreive/<int:pk>/', TimeTableRetrieveUpdateDeleteAPIView.as_view(), name='timetable_retrive'),
    path('timetable/update/<int:pk>/', TimeTableRetrieveUpdateDeleteAPIView.as_view(), name='timetable_update'),
    path('timetable/partial_update/<int:pk>/', TimeTableRetrieveUpdateDeleteAPIView.as_view(), name='timetable_partial_update'),
    path('timetable/delete/<int:pk>/', TimeTableRetrieveUpdateDeleteAPIView.as_view(), name='timetable_delete'),   
    
    path('send-email/', EmailAPI.as_view()),
]