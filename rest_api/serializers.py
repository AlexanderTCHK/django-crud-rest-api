from rest_framework import serializers
from .models import Courses


class CoursesSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"

class CoursesSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ["id", "title"]

class CoursesSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
