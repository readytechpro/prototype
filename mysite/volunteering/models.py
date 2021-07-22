from django.db import models

class VolunteerProject(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class VolunteerProjectDetailCategory(models.Model):
    project = models.ForeignKey(VolunteerProject, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    heading = models.CharField(max_length=150)
    position = models.IntegerField() # position of category within project post

    def __str__(self):
        return f'Category {self.position} "{self.heading}"- {self.project}'


class VolunteerProjectDetail(models.Model):
    detail_category = models.ForeignKey(VolunteerProjectDetailCategory, on_delete=models.CASCADE)
    text = models.TextField()
    position = models.IntegerField() # position of detail within category

    def __str__(self):
        return f'Detail {self.position} - {self.detail_category}'
