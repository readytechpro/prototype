from django.urls import path
from . import views
from .views import ProjectListView

app_name = 'volunteering'

urlpatterns = [
    path('', ProjectListView.as_view(), name='index')
]