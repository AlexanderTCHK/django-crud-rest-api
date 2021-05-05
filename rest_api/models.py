from django.db import models

# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    num_of_lectures = models.IntegerField()


