from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# Function based view
def myview(request):
    return HttpResponse("<h1>Hello World</h1>")

# class based view
class MyView(View):
    name="<h1>Ashish Anand</h1>"
    def get(self,request):
        return HttpResponse(self.name)

