from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView, ListView, CreateView, UpdateView, DeleteView)
from .models import LearningResource
from .forms import LearningResourceCreateForm, LearningResourceUpdateForm
import random 

def index(request):
    if request.user.is_authenticated:
        context = {'user_tracks': LearningResource.objects.filter(user=request.user).count()}
    else:
        context = {'user_tracks': 0}
    return render(request, 'resources/index.html', context)

def get_colors(list_length):
    colors = []

    for item in range(list_length):
        green_color = [28, 153, 84]
        variance_coeff = 0.15
        new_color = []
        for component in green_color:
            value_range = [int(component - (component * variance_coeff)), int(component + (component * variance_coeff))]
            random_value = random.randint(*value_range)
            new_color.append(random_value)

        colors.append(new_color)
    return colors


class LearningResourceListView(ListView):
    model = LearningResource
    template_name = 'resources/learning_resources_list.html'
    context_object_name = 'learning_resources'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        colors = get_colors(len(context['learning_resources']))

        context['learning_resources'] = zip(context['learning_resources'], colors)
        return context

class UserLearningResourceListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = LearningResource
    template_name = 'resources/learning_resources_list.html'
    context_object_name = 'learning_resources'

    def get_queryset(self):
        return LearningResource.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        colors = get_colors(len(context['learning_resources']))

        context['learning_resources'] = zip(context['learning_resources'], colors)
        context['user_resources'] = True
        return context

    def test_func(self):
        queryset = self.get_queryset()
        if queryset.first().user == self.request.user:
            return True
        else:
            return False
        

class LearningResourceDetailView(LoginRequiredMixin, DetailView):
    model = LearningResource

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit'] = self.is_author()
        context['user_tracks'] = LearningResource.objects.filter(user=self.request.user).count()
        return context

    def is_author(self):
        if self.get_object().user == self.request.user:
            return True
        else:
            return False


class LearningResourceCreateView(LoginRequiredMixin, CreateView):
    model = LearningResource
    form_class = LearningResourceCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    
class LearningResourceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LearningResource
    form_class = LearningResourceUpdateForm

    def test_func(self):
        if self.get_object().user == self.request.user:
            return True
        else:
            return False


class LearningResourceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LearningResource
    
    def get_success_url(self):
        return reverse_lazy('resources:all_learning_resources')
    
    def test_func(self):
        if self.get_object().user == self.request.user:
            return True
        else:
            return False

