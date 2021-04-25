import datetime

from django.db import models
from django.contrib.auth.models import User
from datetime import time


from apps.cources.service import validate_round_hour
import datetime as dt
from apps.cources.models import Courses, WorkTime, WEEKDAYS
from apps.cources.service import validate_round_hour
from apps.users.services import TIME_CHOICES


class TeacherWorkTime(models.Model):
    date_time = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.id}, {self.date_time}'

    class Meta:
        verbose_name = 'Рабочие дни'
        verbose_name_plural = 'Рабочие дни'


class Teacher(models.Model):
    user = models.OneToOneField(User, related_name='teacher', on_delete=models.CASCADE)
    cources = models.ManyToManyField(Courses, related_name='teacher')
    work_time = models.ManyToManyField(TeacherWorkTime)
    def __str__(self):
        return str(self.user.first_name)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class StudentHour(models.Model):
    from_hour = models.TimeField(default='0:00')
    cource = models.ForeignKey(
        to=Courses, on_delete=models.CASCADE, related_name='hour', null=True,
    )
    cource_work_time = models.ManyToManyField(TeacherWorkTime, related_name='hour', null=True)

    @property
    def end_hour(self):
        hour = self.from_hour.hour + 1
        time_hour = time(hour)
        print(time_hour)
        return time_hour

    def __str__(self):
        return f'{self.id}. {str(self.from_hour.hour)}:00, {self.cource.name}'

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'


class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    cource = models.ManyToManyField(StudentHour, related_name='student')


    def __str__(self):
        return f'{self.id}, {self.user.first_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'