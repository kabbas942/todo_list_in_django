from django.db import models

# Create your models here.

class todoList(models.Model):
    title = models.CharField(max_length=122)
    description = models.CharField(max_length=122)
    created_at = models.DateField()
    completed = models.DateField()
    
    def __str__(self) :
        return self.title
    
