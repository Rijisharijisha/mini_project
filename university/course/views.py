from django.shortcuts import render
from course.models import *




def vieww(request):
    obj=Course.objects.all()
    return render(request,'courseview.html',{'data':obj})

    

def show(request):
    obj=Syllabus.objects.all()
    return render(request,'syllabusview.html',{'data':obj})

    


                   
