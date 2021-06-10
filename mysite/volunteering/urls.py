from django.urls import path
from . import views
from .views import ProjectListView, ProjectDetailView

app_name = 'volunteering'

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', ProjectListView.as_view(), name='all_volunteer_projects'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]