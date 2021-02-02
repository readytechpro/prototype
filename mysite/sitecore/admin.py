from django.contrib import admin
from .models import CopyText, FrequentQuestion, Page

admin.site.register(Page)
admin.site.register(CopyText)
admin.site.register(FrequentQuestion)
