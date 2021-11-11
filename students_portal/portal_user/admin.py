from django.contrib import admin

# Register your models here.
from .models import Student, Teacher, MarkList
# Register your models here.


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(MarkList)
