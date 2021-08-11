from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse


class CategoryTag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}'


class LearningResource(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255, default='Enter a tag line', null=True)
    description = models.TextField(default='Enter a resource descripiton', null=True)
    tags = models.ManyToManyField(CategoryTag)
    notion_link = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.user:
            return f'{self.title} - [{self.user.username}]'
        else:
            return f'{self.title}'

    def get_absolute_url(self):
        return reverse('resources:resource_detail', kwargs={'pk': self.pk})

