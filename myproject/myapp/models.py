from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, default="")
    date_of_birth = models.DateField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def str(self):
        return f'{self.first_name} {self.last_name}'


# Create your models here.ь
