from django.db import models
from django.contrib import admin
class Football (models.Model):
    pid=models.CharField(max_length=20,help_text="Player ID")
    name=models.CharField(max_length=100)
    team=models.CharField(max_length=100)
    age=models.IntegerField()
    position=models.CharField(max_length=100)

class FootballAdmin(admin.ModelAdmin):
    list_display=('pid','name','team','age','position')
