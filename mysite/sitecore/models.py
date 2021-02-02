from django.db import models

class Page(models.Model):
    label = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.label}'


class CopyText(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True)
    label = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField()
    position = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.page.label}: {self.position}: {self.title[:10]}: {self.text[:7]}'


class FrequentQuestion(models.Model):
    question_text = models.CharField(max_length=150)
    answer_text = models.TextField()
    votes = models.IntegerField()

    def __str__(self):
        return f'{self.votes}: {self.question_text[:10]}'
        