from django.db import models


class SiteSettings(models.Model):
    Photo = models.ImageField(upload_to='img',verbose_name='Your  Photo ')
    NameAndSurname = models.CharField(max_length=999,verbose_name='Name And Surname ')
    Job = models.CharField(max_length=999,verbose_name='Job : Web Developer ')
    Email = models.CharField(max_length=999,verbose_name='Your Email ',blank=True,null=True)
    Address = models.CharField(max_length=999,verbose_name='Your Address ',blank=True,null=True)
    Instagram = models.CharField(max_length=999,verbose_name='Instagram Id ')
    Telegram = models.CharField(max_length=999,verbose_name='Telegram Id ',blank=True,null=True)
    Twitter = models.CharField(max_length=999,verbose_name='Twitter Id ')
    Facebook = models.CharField(max_length=999,verbose_name='Facebook Id ')
    AboutMe = models.TextField(verbose_name='About Me ')



    def __str__(self):
        return f'{self.NameAndSurname}'


