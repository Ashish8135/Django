from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from school.forms import ContactForm
# Create your views here.
# Function based view
def homefun(request):
    return render(request,'school/home.html')

def about(request):
    context={'msg':"Welcome to function based view in django"}
    return render(request,'school/about.html',context=context)

# Class Based View
class home_class_view(View):
    def get(self,request):
        return render(request,'school/home.html')

# Class base view with context in django
class AboutClassView(View):
    def get(self,request):
        context={'msg':"Welcome to class based view in django"}
        return render(request,'school/about.html',context=context)

###############################################

def contactfun(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Thank you for subitting the form")
    else:
        form=ContactForm()
    return render(request,'school/contact.html',{'form':form})


# class Base view 

class ContactClassView(View):
    def get(self,request):
        form=ContactForm()
        return render(request,'school/contact.html',{'form':form})

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Thank you for subitting the form")




