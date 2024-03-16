from django.db import models

# Create your models here.
from users.models import Student


class Notification(models.Model):
    student_id = models.ForeignKey(Student)
    type = models.CharField()
    title = models.CharField()
    message = models.TextField()
    created_time = models.DateTimeField()