"""classView_Prac1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homefun/',views.homefun,name="homefun"),
    path('about/',views.about,name="homefun"),
    path('classhome',views.home_class_view.as_view(),name="classhome"),
    path('classabout',views.AboutClassView.as_view(),name="classabout"),
    path('contactfun/',views.contactfun,name="contactfun"),
    path('ContactClassView/',views.ContactClassView.as_view(),name="ContactClassView"),
]
