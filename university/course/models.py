from django.db import models


class Course(models.Model):
    course=models.CharField(max_length=30)
    c_id=models.AutoField(primary_key=True)

    # class meta:
    #     verbose_name_plural="Course"
    # def __str__(self):
    #         return self.course

class Syllabus(models.Model):
    syllabus=models.CharField(max_length=30,unique=True)
    s_id=models.AutoField(primary_key=True)

    # class meta:
    #     verbose_name_plural="Syllabus"
    # def __str__(self):
    #         return self.syllabus

