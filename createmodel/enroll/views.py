from django.shortcuts import render

# Create your views here.
from enroll.models import Students

def StudentInfo(request):
    stud=Students.objects.all()
    return render(request,'enroll/student.html',{'stu':stud})
