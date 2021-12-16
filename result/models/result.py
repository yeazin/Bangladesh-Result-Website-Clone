from django.db import models

from accounts.models import TimeStamp


class ResultProfile(TimeStamp):

    name = models.CharField(max_length=200,null=True,blank=True,verbose_name='Applicant Name')

    def __str__(self):
        return self.name 