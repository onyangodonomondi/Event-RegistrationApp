from django.db import models
import datetime

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField( default=datetime.date.today)
    description = models.TextField()

    def __str__(self):
        return self.title

class skills(models.Model):
    skill = models.CharField(max_length=100)
    level = models.IntegerField(null=True, blank=True , default=50)


    def __str__(self):
        return self.skill   


class Education(models.Model):
    course = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField( default=datetime.date.today)
    description = models.TextField()

    def __str__(self):
        return self.course

