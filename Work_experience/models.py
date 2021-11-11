from django.db import models

class WorkExperience(models.Model):
    Date = models.CharField(max_length=999,verbose_name='Date ')
    Title = models.CharField(max_length=999,verbose_name='Title ')
    Description = models.TextField(verbose_name='Description ')

    def __str__(self):
        return f'{self.Title}'
