from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    amount_of_lessons = models.IntegerField()
    price = models.IntegerField(blank=True)

    def __str__(self):
        return self.name