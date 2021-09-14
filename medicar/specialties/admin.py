from django.contrib import admin

from medicar.specialties.models import Specialty


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass

