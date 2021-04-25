from datetime import date

from rest_framework.response import Response
from rest_framework import serializers

from apps.users.models import Teacher, TeacherWorkTime, Student, StudentHour


class StudentHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHour
        fields = ('from_hour', 'cource')


class TeacherWorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherWorkTime
        fields = ('id', 'date_time')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('user',)


class CreateCourceSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    cource = StudentHourSerializer()
    timeout = serializers.DateField(default=date.today())
    class Meta:
        model = Student
        fields = ('cource', 'user_id', 'timeout')

    def create(self, validated_data):
        timeout = validated_data.pop('timeout')
        cource_id = validated_data.pop('cource')
        cource, cource_created = StudentHour.objects.get_or_create(**cource_id)
        student, created = Student.objects.get_or_create(user_id=validated_data.pop('user_id'))

        if not student.cource.first():
            student.cource.add(cource)
            print('ya tut')

        elif cource_created:
            # finding the least busy teacher
            least_busy_teacher = cource.cource.teacher.first()
            work_time = []

            for teacher in cource.cource.teacher.all():
                if len(least_busy_teacher.cources.all()) < len(teacher.cources.all()):
                    least_busy_teacher = teacher
            for t in cource.cource.work_time.all():
                if t.date_time >= timeout:
                    work_time.append(t.id)
            cource.cource_work_time.add(*work_time)


            dict_cource_id = dict(cource_id)
            for c in student.cource.all():
                if c.from_hour.hour != dict_cource_id.get('from_hour').hour:
                    student.cource.add(cource)
                    break

        return student