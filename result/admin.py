from django.contrib import admin

# Register your models here.
from result.models.result import ResultProfile
from result.models.initial import Year

admin.site.register(ResultProfile)
admin.site.register(Year)