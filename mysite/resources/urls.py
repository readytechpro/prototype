from django.urls import path
from . import views
from .views import LearningResourceListView

app_name = 'resources'

urlpatterns = [
    path('', views.index, name='index'), 
    path('all/', LearningResourceListView.as_view(), name='all_learning_resources'),
]