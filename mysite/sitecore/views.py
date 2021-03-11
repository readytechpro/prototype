from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import FrequentQuestion, CopyText, Page, SectionTitle

def index(request):
    return render(request, 'sitecore/index.html')

def about_program(request, program_name):
    page = Page.objects.get(label=program_name)
    section_structures = []
    sections = SectionTitle.objects.filter(page__label=program_name).order_by('position')
    for section in sections:
        section_copy_items = CopyText.objects.filter(title=section).order_by('position')
        section_structures.append((section, section_copy_items))
    
    context = {'sections': section_structures, 'page': page}
    return render(request, 'sitecore/about_program.html', context)


class FAQListView(ListView):
    model = FrequentQuestion
    template_name = 'sitecore/faq.html'
    context_object_name = 'faqs'
    ordering = ['votes']
