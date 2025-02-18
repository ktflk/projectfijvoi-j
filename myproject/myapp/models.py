from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    adress = models.CharField(max_length=50)
    date_of_birth = models.DateField(max_length=10)
    created_at = models.DateTimeField(max_length=20)
    updated_at = models.DateTimeField(max_length=20)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Create your models here.
