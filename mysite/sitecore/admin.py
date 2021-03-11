from django.contrib import admin
from .models import CopyText, FrequentQuestion, Page, SectionTitle

admin.site.register(Page)
admin.site.register(CopyText)
admin.site.register(FrequentQuestion)
admin.site.register(SectionTitle)
