from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    illness = models.CharField(max_length=255)
    address = models.TextField()
    patient_id = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=10, default='Admitted')
    date_admitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
