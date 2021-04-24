from django.db import models

from apps.cources.models import Courses


class Events(models.Model):
    day = models.DateField()
    start = models.TimeField()
    finish = models.TimeField()
    teacher = models.ForeignKey("users.Teacher", on_delete=models.CASCADE)
    cource = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cource)