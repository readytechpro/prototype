from django.shortcuts import render
from django.views.generic import ListView
from .models import LearningResource

def index(request):
    return render(request, 'resources/index.html')


class LearningResourceListView(ListView):
    model = LearningResource
    template_name = 'resources/learning_resources_list.html'
    context_object_name = 'learning_resources'


