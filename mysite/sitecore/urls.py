from django.urls import path
from . import views
from .views import FAQListView

app_name = 'sitecore'

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', FAQListView.as_view(), name='faq'),
    path('about/<slug:program_name>/', views.about_program, name='about-program-detail'),
]