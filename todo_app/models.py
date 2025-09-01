from django.db import models

class Todo(models.Model): #PAscalCase
    title = models.CharField(max_length=255) #varchar , char

    def __str__(self):
        return self.title