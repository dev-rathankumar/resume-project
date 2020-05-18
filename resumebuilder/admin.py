from django.contrib import admin
from .models import Resume


admin.site.site_header = 'CVforTwenty5'

class ResumeA(admin.ModelAdmin):
    list_display = ['email', 'created_on']

# Register your models here.
admin.site.register(Resume, ResumeA)
