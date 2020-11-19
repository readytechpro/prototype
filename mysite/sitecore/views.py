from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import FrequentQuestion, CopyText

def index(request):
    return render(request, 'sitecore/index.html')

def about_resources_program(request):
    about_copy = CopyText.objects.get(label='resources')
    context = {'about_copy': about_copy}
    return render(request, 'sitecore/about_program.html', context)

def about_community_program(request):
    about_copy = CopyText.objects.get(label='community')
    context = {'about_copy': about_copy}
    return render(request, 'sitecore/about_program.html', context)

def about_collaboration_program(request):
    about_copy = CopyText.objects.get(label='collaboration')
    context = {'about_copy': about_copy}
    return render(request, 'sitecore/about_program.html', context)

def about_opportunities_program(request):
    about_copy = CopyText.objects.get(label='opportunities')
    context = {'about_copy': about_copy}
    return render(request, 'sitecore/about_program.html', context)


class FAQListView(ListView):
    model = FrequentQuestion
    template_name = 'sitecore/faq.html'
    context_object_name = 'faqs'
    ordering = ['votes']
