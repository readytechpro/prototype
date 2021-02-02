from django.urls import path
from . import views
from .views import FAQListView

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', FAQListView.as_view(), name='faq'),
    path('about/<str:program_name>/', views.about_program, name='about-program-detial'),
]