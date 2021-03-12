from django.shortcuts import render
from django.views.generic import ListView
from .models import (
    VolunteerProject, VolunteerProjectDetail, VolunteerProjectDetailCategory
)

class ProjectListView(ListView):
    model = VolunteerProject
    template_name = 'volunteering/index.html'
    context_object_name = 'projects'
