from django.db import models

from accounts.models import TimeStamp



class Year(TimeStamp):
    year = models.IntegerField(null=True,verbose_name='Calender year')

    def __str__(self):
        return str(self.year)


    class Meta:
        verbose_name = 'Year'