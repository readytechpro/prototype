from django.db import models

class LearningResource(models.Model):
    title = models.CharField(max_length=100)
    notion_link = models.URLField()

    def __str__(self):
        return f'{self.title}'

