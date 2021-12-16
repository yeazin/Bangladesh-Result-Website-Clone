from django.db import models


# Initials models 
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Is Active')

    class Meta:
        abstract = True
