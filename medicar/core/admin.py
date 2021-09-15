from django.contrib import admin

from medicar.core.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass
