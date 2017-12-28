from django.db import models

class User(models.Model):
    SEX = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 255)
    full_name = models.CharField(max_length = 30)
    bod = models.DateField()
    sex = models.CharField(max_length = 1, choices = SEX)
    address = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)
    image_path = models.FilePathField(max_length = 255)

class Admin(User):
    pass

class Dentist(User):
    pass

class Patient(User):
    expiration_time = models.DateTimeField()

class MedicalHistory(models.Model):
    operations = models.BooleanField()
    nursing = models.BooleanField()
    pregnant = models.BooleanField()

class DentalHistory(models.Model):
    bad_breath = models.BooleanField()
    sensitive_teeth = models.BooleanField()

class DentalService(models.Model):
    name = models.CharField(max_length = 30)
    price = models.BigIntegerField()
    description = models.TextField(max_length = 255)

class DentalRecord(models.Model):
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    note = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentists = models.ManyToManyField(Dentist)
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE)
    dental_history = models.ForeignKey(DentalHistory, on_delete=models.CASCADE)

class Examination(models.Model):
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    note = models.TextField()
    log = models.TextField()
    dental_record = models.ForeignKey(DentalRecord, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    dental_services = models.ManyToManyField(DentalService)
