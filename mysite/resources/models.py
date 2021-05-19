from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse

class LearningResource(models.Model):
    title = models.CharField(max_length=100)
    notion_link = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.user:
            return f'{self.title} - [{self.user.username}]'
        else:
            return f'{self.title}'

    def get_absolute_url(self):
        return reverse('resources:resource_detail', kwargs={'pk': self.pk})

