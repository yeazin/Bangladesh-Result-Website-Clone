from django.db import models

from accounts.models import TimeStamp


class ResultProfile(TimeStamp):

    rollNumber = models.IntegerField(verbose_name='Roll Number',unique=True,null=True)
    regiNumber = models.IntegerField(verbose_name='Regi Number',null=True)
    
    name = models.CharField(max_length=200,null=True,blank=True,verbose_name='Applicant Name')
    fName = models.CharField(max_length=200, null=True,blank=True,verbose_name='Applicant Father`s Name')
    dob = models.DateField(null=True,blank=True,auto_now_add=False,verbose_name='Applicant Date of Birth')


    className = models.CharField(max_length=100,null=True,blank=True,verbose_name='Class Name')
    groupName = models.CharField(max_length=100,blank=True,null=True,verbose_name='Group Name')




    def __str__(self):
        return self.name 
