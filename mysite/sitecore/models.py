from django.db import models

class CopyText(models.Model):
    label = models.CharField(max_length=25)
    text = models.TextField()

    def __str__(self):
        return f'{self.label}: {self.text[:10]}'


class FrequentQuestion(models.Model):
    question_text = models.CharField(max_length=150)
    answer_text = models.TextField()
    votes = models.IntegerField()

    def __str__(self):
        return f'{self.votes}: {self.question_text[:10]}'
        