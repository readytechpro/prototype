from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import FrequentQuestion

def index(request):
    return render(request, 'sitecore/index.html')

class FAQListView(ListView):
    model = FrequentQuestion
    template_name = 'sitecore/faq.html'
    context_object_name = 'faqs'
    ordering = ['votes']
