from django.urls import path
from . import views
from resources.views import (
    LearningResourceListView, LearningResourceCreateView, 
    LearningResourceUpdateView, LearningResourceDeleteView,
    LearningResourceDetailView, UserLearningResourceListView,
)

app_name = 'resources'

urlpatterns = [
    path('', views.index, name='index'), 
    path('all/', LearningResourceListView.as_view(), name='all_learning_resources'),
    path('my_resources/', UserLearningResourceListView.as_view(), name='my_learning_resources'),
    path('new/', LearningResourceCreateView.as_view(), name='resource_create'),
    path('<int:pk>/', LearningResourceDetailView.as_view(), name='resource_detail'),
    path('<int:pk>/update/', LearningResourceUpdateView.as_view(), name='resource_update'),
    path('<int:pk>/delete/', LearningResourceDeleteView.as_view(), name='resource_delete' ),
]