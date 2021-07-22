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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        related_detail_categories = VolunteerProjectDetailCategory.objects.filter(
            project=project).order_by('position')
        details_structure = {}
        for category in related_detail_categories:
            related_details = VolunteerProjectDetail.objects.filter(
                detail_category=category).order_by('position').values_list('text', flat=True)
            details_structure[f'{category.heading}'] = related_details

        context['categories_detials'] = details_structure
        return context

