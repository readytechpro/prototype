from django.contrib import admin
from .models import (
    VolunteerProject, VolunteerProjectDetail, VolunteerProjectDetailCategory,
    CategoryTag
)

admin.site.register(VolunteerProject)
admin.site.register(VolunteerProjectDetail)
admin.site.register(VolunteerProjectDetailCategory)
admin.site.register(CategoryTag)