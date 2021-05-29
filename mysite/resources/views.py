from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView, ListView, CreateView, UpdateView, DeleteView)
from .models import LearningResource

def index(request):
    if request.user.is_authenticated:
        context = {'user_tracks': LearningResource.objects.filter(user=request.user).count()}
    else:
        context = {'user_tracks': 0}
    return render(request, 'resources/index.html', context)


class LearningResourceListView(ListView):
    model = LearningResource
    template_name = 'resources/learning_resources_list.html'
    context_object_name = 'learning_resources'


class UserLearningResourceListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = LearningResource
    template_name = 'resources/learning_resources_list.html'
    context_object_name = 'learning_resources'

    def get_queryset(self):
        return LearningResource.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
    fields = ['title', 'notion_link']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    
class LearningResourceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LearningResource
    fields = ['title', 'notion_link']

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

