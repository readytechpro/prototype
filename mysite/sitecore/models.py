from django.db import models

class CopyText(models.Model):
    label = models.CharField(max_length=25)
    text = models.TextField()

    def __str__(self):
        return f'{self.label}: {self.text[:10]}'
        