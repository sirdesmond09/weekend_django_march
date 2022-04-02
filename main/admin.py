from django.contrib import admin
from main.models import Student

# Register your models here.

# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "course", "student_num", "date_joined", 'is_active']
    list_editable = ['is_active',]
    list_filter = ['is_active', "course","date_joined"]
    list_per_page = 5
    search_fields = ['course', "name"]
    