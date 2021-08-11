from django import forms
from .models import LearningResource, CategoryTag

class LearningResourceUpdateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=CategoryTag.objects.all(), required=False)

    class Meta:
        model = LearningResource
        fields = ['title', 'notion_link', 'tagline', 'description', 'tags']


class LearningResourceCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=CategoryTag.objects.all(), required=False)

    class Meta:
        model = LearningResource
        fields = ['title', 'notion_link', 'tagline', 'description', 'tags']
