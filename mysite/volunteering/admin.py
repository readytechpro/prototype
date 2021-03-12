from django.contrib import admin
from .models import (
    VolunteerProject, VolunteerProjectDetail, VolunteerProjectDetailCategory 
)

admin.site.register(VolunteerProject)
admin.site.register(VolunteerProjectDetail)
admin.site.register(VolunteerProjectDetailCategory)
