from django.shortcuts import render
from enroll.forms import StudentRegister
# Create your views here.
def FormData(request):
    fm=StudentRegister()
    return render(request,'enroll/registration.html',{'forms':fm})

