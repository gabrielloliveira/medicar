from django.contrib import admin

from medicar.schedule.models import Schedule, ScheduleTime


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["doctor", "date"]
    list_filter = ["doctor", "date"]
    search_fields = ["doctor__name"]


@admin.register(ScheduleTime)
class ScheduleTimeAdmin(admin.ModelAdmin):
    list_display = ["time"]
