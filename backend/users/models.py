from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Guardian(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120) 
    phone_number = models.CharField(max_length=15)
    phone_number_2 = models.CharField(max_length=15)
    email_address = models.EmailField()
    city = models.CharField()
    state = models.CharField()
    address = models.CHarField()

class Courses(models.Model):        
    name = models.CharField(max_length=120, blank=False)
    duration = models.PositiveIntegerField(
        validator=[MinValueValidator(4), MaxValueValidator(6)]
    )
    faculty = models.CharField(blank=False)

class Role(models.Model):
    name = models.CharField()

class Student(models.Model):
    guardian_id = models.ForeignKey(Guardian)
    course_id = models.ForeignKey()
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    matric_number = models.CharField()
    entry_session = models
    jaja_number = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=12)
    
class Staff(models.Model):
    role_id = models.ForeignKey(Role)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField()
    

