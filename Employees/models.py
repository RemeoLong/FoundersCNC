from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now())


class Location(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField(max_length=5)
    contact_first_name = models.CharField(max_length=50)
    contact_last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()


class Machine(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


class Revision(models.Model):
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    revision = models.IntegerField()
    file = models.FileField(upload_to='static/revision', blank=True)


class MachineDocument(models.Model):
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    document = models.FileField(upload_to='static/machine_documents', null=True)
    created_at = models.DateTimeField(default=datetime.now())


class Manual(models.Model):
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    manual = models.FileField(upload_to='static/manuals', null=True)
    video = models.FileField(upload_to='static/videos', null=True)
    created_at = models.DateTimeField(default=datetime.now())


class ServiceOrder(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    invoice = models.FileField(upload_to='static/invoices', null=True)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now())


class Employee(models.Model):
    status_choice = (
        ('Employed', 'Employed'),
        ('Laid Off', 'Laid Off'),
        ('Terminated', 'Terminated'),
        ('Vacation', 'Vacation')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField(max_length=5)
    phone_number = models.BigIntegerField()
    status = models.CharField(max_length=15, choices=status_choice)
    created_at = models.DateTimeField(default=datetime.now())


class EmployeeW2(models.Model):
    employees_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    w2_1099 = models.FileField(blank=True)


class EmployeePayStub(models.Model):
    employees_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_stub = models.FileField(blank=True)


class ServiceCall(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    employees_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    appointment = models.DateTimeField()
    status = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=datetime.now())


class Merchant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField(max_length=5)
    contact_first_name = models.CharField(max_length=50)
    contact_last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()


class MerchantInvoice(models.Model):
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    total = models.FloatField()
    invoice = models.FileField(upload_to='static/merchant_invoices', null=True)
    created_at = models.DateTimeField(default=datetime.now())
