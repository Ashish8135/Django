from django.urls import path
from enroll import views
urlpatterns=[
    path('stud/',views.StudentInfo,name="stud"),
]