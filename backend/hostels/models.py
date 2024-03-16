from django.db import models

# Create your models here.

class Hostel(models.Model):
    name = models.CharField(max_length=120)
    gender = models.TextField(blank=True, null=True)
    

class Block(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField()
    hostel_id = models.ForeignKey(Hostel, on_delete=models.CASCADE)


class Room(models.Model):
    number = models.IntegerField()
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE)
    capacity = models.IntegerField

    # Implement Function to get the Room Name relating to the HOstel and Block