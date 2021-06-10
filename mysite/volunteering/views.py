from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import (
    VolunteerProject, VolunteerProjectDetail, VolunteerProjectDetailCategory
)

def index(request):
    return render(request, 'volunteering/index.html')


class ProjectListView(ListView):
    model = VolunteerProject
    template_name = 'volunteering/volunteer_projects_list.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = VolunteerProject
    template_name = 'volunteering/volunteer_project_detail.html'
    context_object_name = 'project'

