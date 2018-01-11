from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class DentalClinicUser(models.Model):
    SEX = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    ROLE = (
        ('a', 'Admin'),
        ('d', 'Dentist'),
        ('p', 'Patient'),
    )

    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
    )
    role = models.CharField(
        max_length = 1,
        choices = ROLE,
        null = False,
        default = 'p',
    )
    bod = models.DateField(
        null = True,
        blank = True,
    )
    sex = models.CharField(
        max_length = 1,
        choices = SEX,
        null = True,
        blank = True,
    )
    address = models.CharField(
        max_length = 255,
        null = True,
        blank = True,
    )
    phone_number = models.CharField(
        max_length = 30,
        null = True,
        blank = True,
    )
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.__str__()

@receiver(post_save, sender = User)
def create_dental_clinic_user(sender, instance, created, **kwargs):
    if created:
        DentalClinicUser.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_dental_clinic_user(sender, instance, **kwargs):
    instance.dentalclinicuser.save()

class MedicalHistory(models.Model):
    operations = models.BooleanField(default = False)
    nursing = models.BooleanField(default = False)
    pregnant = models.BooleanField(default = False)

class DentalHistory(models.Model):
    bad_breath = models.BooleanField(default = False)
    sensitive_teeth = models.BooleanField(default = False)

class DentalService(models.Model):
    name = models.CharField(
        max_length = 30,
        null = True,
        blank = True,
    )
    price = models.BigIntegerField(
        null = True,
        blank = True,
    )
    description = models.TextField(
        max_length = 255,
        null = True,
        blank = True,
    )

    def __str__(self):
        return self.name

class DentalRecord(models.Model):
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now_add = True)
    note = models.TextField(
        null = True,
        blank = True,
    )
    patient = models.OneToOneField(
        DentalClinicUser,
        on_delete = models.CASCADE,
        related_name = 'patient',
    )
    dentists = models.ManyToManyField(
        DentalClinicUser,
        related_name = 'dentists',
    )
    medical_history = models.OneToOneField(
        MedicalHistory,
        on_delete = models.CASCADE,
    )
    dental_history = models.OneToOneField(
        DentalHistory,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return '{} {}'.format(self.patient, self.dentists)

class Examination(models.Model):
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now_add = True)
    note = models.TextField(
        null = True,
        blank = True,
    )
    log = models.TextField(
        null = True,
        blank = True,
    )
    dental_record = models.ForeignKey(
        DentalRecord,
        on_delete = models.CASCADE,
    )
    dentist = models.ForeignKey(
        DentalClinicUser,
        on_delete = models.CASCADE,
    )
    dental_services = models.ManyToManyField(DentalService)

