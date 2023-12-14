from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    age = models.IntegerField(validators=[MinValueValidator(0)])
    fatherName= models.CharField(max_length=150)
    motherName= models.CharField(max_length=150)
    phone = models.IntegerField()
    in_class =  models.CharField(max_length=100)
    nationality  = models.CharField(max_length=100)
    address = models.CharField(max_length=350)
    chemisrty_grade = models.IntegerField(null=True)

 

    def __str__(self):
        return self.name
    
class Chemistry(models.Model):
    teacher= models.CharField(max_length=150)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True )
    
    date = models.DateTimeField()

 
    def __str__(self):
        return self.teacher 


