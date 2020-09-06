from django.contrib import admin
from enroll.models import Students
# Register your models here.
# admin.site.register(Students)

@admin.register(Students)
class ModelAdminStudent(admin.ModelAdmin):
    list_display = ['stuid', 'stuname', 'stuemail', 'stupass', 'comment']

# admin.site.register(Students, ModelAdminStudent)