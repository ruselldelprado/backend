from django.db import models

# Create your models here.
# Create your models here.
class Incident(models.Model):
    date = models.DateField()
    time_of_call = models.TimeField()
    details = models.CharField(max_length=200)
    caller = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    action_taken = models.CharField(max_length=200)
    time_of_dispatch = models.TimeField()
    responded_by = models.CharField(max_length=100)
    back_to_base = models.TimeField()
    radio_or_telephone = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
