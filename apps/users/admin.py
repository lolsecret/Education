from django.contrib import admin

# Register your models here.
from apps.users.models import Teacher, Student, StudentHour, TeacherWorkTime

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentHour)
admin.site.register(TeacherWorkTime)

