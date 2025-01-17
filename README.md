# Ex02 Django ORM Web Application
## Date: 02.11.2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
Admin.py

from django.contrib import admin
from .models import Football,FootballAdmin
admin.site.register(Football,FootballAdmin)

Models.py

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

```

## OUTPUT
![Screenshot 2023-11-02 214437](https://github.com/karthick-2003-coder/ORM/assets/135232854/c702d1e6-1609-4526-9abe-2a0713d8f172)




## RESULT
Thus the program for creating a database using ORM hass been executed successfully
