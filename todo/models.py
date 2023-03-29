from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # ID/PK is automatically generated

    def __str__(self):
        return self.title
