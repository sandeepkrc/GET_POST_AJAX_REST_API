from django.db import models
from django.db import models

class Students(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.first_name 
