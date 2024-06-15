from django.urls import path
from . import views


urlpatterns = [
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login/', views.teacher_login),
    path('category/', views.CategoryList.as_view()),

    # teacher courese
    path('course/', views.CourseList.as_view()),
    path('chapter/', views.ChapterList.as_view()),
    # single teacher courses
    path('teacher-course/<int:teacher_id>/', views.TeacherCourseList.as_view()),
]