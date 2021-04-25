from rest_framework import serializers

from apps.cources.models import Courses, WorkTime
from apps.users.models import Student
from apps.users.serializers import TeacherSerializer


class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = ('id', 'date_time')


class CourceSerializer(serializers.ModelSerializer):
    work_time = WorkTimeSerializer(many=True)
    teacher = TeacherSerializer(many=True)

    class Meta:
        model = Courses
        fields = ('amount_of_lessons', 'name', 'id', 'work_time', 'teacher')
