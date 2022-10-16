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

class skill(models.Model):
    skill = models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/skills', null= True, blank = True)
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

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    img=models.ImageField(upload_to='images/blog', null= True, blank = True)

    def __str__(self):
        return self.title

class portfolio(models.Model):
    title = models.CharField(max_length=100)
    img=models.ImageField(upload_to='images/portfolio', null= True, blank = True)

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    