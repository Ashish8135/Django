from django import forms

class StudentRegister(forms.Form):
    Uname=forms.CharField()
    Uemail=forms.EmailField()
    Upass=forms.CharField()
    UconPass=forms.CharField()
