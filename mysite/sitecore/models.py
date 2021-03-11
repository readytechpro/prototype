from django.db import models
from django.utils.text import slugify

class Page(models.Model):
    title = models.CharField(max_length=50)
    label = models.SlugField(max_length=50, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.label:
            self.label = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.label}'


class SectionTitle(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    position = models.IntegerField(default=0) #position of section witin page

    def __str__(self):
        return f'{self.title} ({self.page}, position {self.position})'


class CopyText(models.Model):
    title = models.ForeignKey(SectionTitle, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    position = models.IntegerField(default=0) #position of copy within section

    def __str__(self):
        
        return f'{self.text[:30]}, {self.title}'


class FrequentQuestion(models.Model):
    question_text = models.CharField(max_length=150)
    answer_text = models.TextField()
    votes = models.IntegerField()

    def __str__(self):
        return f'{self.votes}: {self.question_text[:10]}'
        