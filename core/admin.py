from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Professor, Course, Department

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Department)
