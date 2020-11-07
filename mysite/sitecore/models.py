from django.db import models

class CopyText(models.Model):
    label = models.CharField(max_length=25)
    text = models.TextField()

    def __str__(self):
        return f'{self.label}: {self.text[:10]}'


class FrequentQuestion(CopyText):
    question_text = models.CharField(max_length=150)
    votes = models.IntegerField()

    @property
    def answer_text(self):
        return self.text

    def __str__(self):
        return f'{self.votes} - {self.label}: {self.question_text[:10]}'
        