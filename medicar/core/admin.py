from django.contrib import admin

from medicar.core.models import Doctor, MedicalAppointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name", "specialty_name"]
    list_filter = ["specialty__name"]
    search_fields = ["name"]


@admin.register(MedicalAppointment)
class MedicalAppointmentAdmin(admin.ModelAdmin):
    list_display = ["doctor", "date", "time"]
    list_filter = ["doctor"]
    search_fields = ["doctor__name"]
