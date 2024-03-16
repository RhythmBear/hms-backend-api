from django.db import models

from users.models import Student
from hostels.models import Room, Hostel

# Create your models here.

class Allocation(models.Model):
    room_id = models.ForeignKey(Room)
    student_id = models.ForeignKey(Student)
    staff_id = models.ForeignKey(Staff)
    

    def get_session():
        pass 



class Application(models.Model):
    class Status(models.TextChoices):
        ACCEPTED = "Approved"
        PENDING = "Pending"
        REJECTED = "Rejected"
        

    student_id = models.ForeignKey(Student)
    hostel_id = models.ForeignKey(Hostel)
    status = models.CharField(choices=Status)
    
    def get_session():
        pass       


class ElligibleStaylites(models.Model):
    student_id = models.ForeignKey(Student)
    status = models.BooleanField(blank=False)
    def get_session():
        pass 


from django.utils import timezone

class Document(models.Model):
    class DocType(models.TextChoices):
        SCHOOL_FEES = "Approved"
        SIGNATURE = "Signature"
        ACCOMODATION_RECIEPT = "accomodation_reciept"

    student_id = models.IntegerField()  # Assuming student ID is an integer
    document_type = models.CharField(max_length=20, choices=DocType)
    url = models.URLField()  # Stores the URL of the uploaded document
    uploaded_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Document for Student ID: {self.student_id} - {self.document_type}"