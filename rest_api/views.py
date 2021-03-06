from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Courses
from .serializers import CoursesSerializerCreate, CoursesSerializerList, CoursesSerializerDetail




class CoursesCreate(generics.CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializerCreate

class CoursesList(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializerList
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'start_date', 'end_date']

class CoursesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializerDetail
