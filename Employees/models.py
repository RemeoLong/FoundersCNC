from django.contrib.auth.models import User
from django.db import models


class Employees(models.Model):
    roles_choice = (
        ('Owner', 'Owner'),
        ('Employee', 'Employee')
    )

    status_choice = (
        ('Employed', 'Employed'),
        ('Laid Off', 'Laid Off'),
        ('Terminated', 'Terminated'),
        ('Vacation', 'Vacation')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=10)
    phone_number = models.BigIntegerField()
    roles = models.CharField(max_length=50, choices=roles_choice)
    status = models.CharField(max_length=15, choices=roles_choice)

