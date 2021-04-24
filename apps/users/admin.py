from django.contrib import admin

# Register your models here.
from apps.users.models import Teacher, Student

admin.site.register(Teacher)
admin.site.register(Student)