from django.db import models
from django.contrib.auth.models import User
from datetime import date

from apps.cources.models import Courses

WEEKDAYS = [
    (1, ("Monday")),
    (2, ("Tuesday")),
    (3, ("Wednesday")),
    (4, ("Thursday")),
    (5, ("Friday")),
    (6, ("Saturday")),
    (7, ("Sunday")),
]


class WorkTime(models.Model):
    weekday = models.IntegerField(
        choices=WEEKDAYS,
        unique=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()


class Teacher(models.Model):
    user = models.OneToOneField(User, related_name='teacher', on_delete=models.CASCADE)
    cources = models.ManyToManyField(Courses)
    work_time = models.ManyToManyField(WorkTime)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)


class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
