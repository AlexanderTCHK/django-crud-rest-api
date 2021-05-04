from django.shortcuts import render

from rest_framework import generics
from .models import Courses
from .serializers import CoursesSerializerCreate, CoursesSerializerList, CoursesSerializerDetail

# Create your views here.
class CoursesCreate(generics.CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializerCreate

# class CoursesList(generics.ListAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CoursesSerializerList

class CoursesList(generics.ListAPIView):
    serializer_class = CoursesSerializerList

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Courses.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset

class CoursesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializerDetail

    # def get_queryset(self):
    #     course_id = Courses.objects.get(pk=self.kwargs['pk'])
    #     print("______________")
    #     print(type(course_id))
    #     print(type(course_id))
    #     return Courses.objects.filter(id=course_id)

