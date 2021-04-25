import datetime

from django.db import models

WEEKDAYS = [
    (1, "Понедельник"),
    (2, "Вторник"),
    (3, "Среда"),
    (4, "Четверг"),
    (5, "Пятница"),
    (6, "Суббота"),
    (7, "Воскресенье"),
]


class WorkTime(models.Model):
    date_time = models.DateField(verbose_name='Дата', default=datetime.datetime.now)

    def __str__(self):
        return f'{self.id}, {self.date_time}'

    class Meta:
        verbose_name = 'Рабочие дни'
        verbose_name_plural = 'Рабочие дни'


class Courses(models.Model):
    name = models.CharField(verbose_name='Название курса', max_length=150)
    amount_of_lessons = models.IntegerField(verbose_name='Количество занятий', default=1)
    work_time = models.ManyToManyField(
        verbose_name='Даты занятий',
        to=WorkTime, related_name='course'
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'