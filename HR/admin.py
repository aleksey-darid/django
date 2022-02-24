from django.contrib import admin
from django.contrib.admin import ModelAdmin

from HR.models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(ModelAdmin):
    pass
