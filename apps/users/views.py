from datetime import datetime
from time import strptime
from time import mktime
from dateutil import parser
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics

from apps.users.models import Student, StudentHour
from apps.users.serializers import CreateCourceSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = CreateCourceSerializer

    def create(self, request, *args, **kwargs):
        timeout = request.data.pop('timeout')
        cource_id = request.data.pop('cource')
        cource, cource_created = StudentHour.objects.get_or_create(from_hour=cource_id['from_hour'], cource_id=cource_id['cource'])
        student, created = Student.objects.get_or_create(user_id=request.data.pop('user_id'))

        if not student.cource.first():
            student.cource.add(cource)

        elif cource_created:
            # finding the least busy teacher
            least_busy_teacher = cource.cource.teacher.first()
            work_time = []

            for teacher in cource.cource.teacher.all():
                if len(least_busy_teacher.cources.all()) < len(teacher.cources.all()):
                    least_busy_teacher = teacher
            for t in cource.cource.work_time.all():
                if t.date_time >= parser.parse(timeout).date():
                    work_time.append(t.id)
            cource.cource_work_time.add(*work_time)

            #check at the time of courses
            dict_cource_id = dict(cource_id)
            for c in student.cource.all():
                if c.from_hour.hour != dict_cource_id.get('from_hour')[:2]:
                    student.cource.add(cource)
                    break

        return Response(f'Вы записались на {cource.cource.name}. Время: {cource.cource_work_time.all()}')