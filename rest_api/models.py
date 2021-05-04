from django.db import models

# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    num_of_lectures = models.IntegerField()
    # created = models.DateTimeField(auto_now_add=True)
    #
    # class Meta:
    #     ordering = ['-created']

    # def __str__(self):
    #     return self.title


