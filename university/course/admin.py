from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display=['course']

class syllabusAdmin(admin.ModelAdmin):
    list_display=['syllabus']



admin.site.register(Course,CourseAdmin)
admin.site.register(Syllabus,syllabusAdmin)

