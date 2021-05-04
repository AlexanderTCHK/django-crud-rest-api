from django.urls import path
from rest_api import views


urlpatterns = [
    path('courses_create', views.CoursesCreate.as_view()),
    path('courses_list', views.CoursesList.as_view()),
    path('courses_list/<int:pk>', views.CoursesDetail.as_view()),

    # Temporary code. Adding a trailing slash to path to avoid testing issues.
    path('courses_create/', views.CoursesCreate.as_view()),
    path('courses_list/', views.CoursesList.as_view()),
    path('courses_list/<int:pk>/', views.CoursesDetail.as_view()),
]
