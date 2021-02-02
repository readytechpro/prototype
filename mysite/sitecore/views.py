from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import FrequentQuestion, CopyText, Page

def index(request):
    return render(request, 'sitecore/index.html')

def about_program(request, program_name):
    page = Page.objects.get(label=program_name)
    copy_items = CopyText.objects.filter(page__label=program_name).order_by('position')
    context = {'segments': copy_items, 'page': page}
    return render(request, 'sitecore/about_program.html', context)


class FAQListView(ListView):
    model = FrequentQuestion
    template_name = 'sitecore/faq.html'
    context_object_name = 'faqs'
    ordering = ['votes']
