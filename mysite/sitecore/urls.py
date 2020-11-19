from django.urls import path
from . import views
from .views import FAQListView

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', FAQListView.as_view(), name='faq'),
    path('resources/', views.about_resources_program, name='about-resources'),
    path('community/', views.about_community_program, name='about-community'),
    path('collaboration/', views.about_collaboration_program, name='about-collaboration'),
    path('opportunities/', views.about_opportunities_program, name='about-opportunities'),
]