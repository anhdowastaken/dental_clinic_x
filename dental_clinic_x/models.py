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
        ('u', 'Unknown'),
    )

    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
    )
    role = models.CharField(
        max_length = 1,
        choices = ROLE,
        null = False,
        default = 'u',
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

    def is_admin(self):
        if self.role == 'a':
            return True
        else:
            return False

    def is_dentist(self):
        if self.role == 'd':
            return True
        else:
            return False

    def is_patient(self):
        if self.role == 'p':
            return True
        else:
            return False

@receiver(post_save, sender = User)
def create_dental_clinic_user(sender, instance, created, **kwargs):
    if created:
        DentalClinicUser.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_dental_clinic_user(sender, instance, **kwargs):
    instance.dentalclinicuser.save()

CURRENCY = (
    ('USD', 'US Dollar'),
    ('VND', 'Vietnam Dong'),
)

class DentalService(models.Model):
    name = models.CharField(
        max_length = 30,
        unique = True,
        null = True,
        blank = True,
    )
    price = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        default = 0,
        null = True,
        blank = True,
    )
    currency = models.CharField(
        max_length = 3,
        choices = CURRENCY,
        default = 'USD',
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

    medical_history_operations = models.BooleanField(default = False)
    medical_history_nursing = models.BooleanField(default = False)
    medical_history_pregnant = models.BooleanField(default = False)

    dental_history_bad_breath = models.BooleanField(default = False)
    dental_history_sensitive_teeth = models.BooleanField(default = False)

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
    dental_services = models.ManyToManyField(DentalService, through='DentalServiceQuantity')

class DentalServiceQuantity(models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    dental_service = models.ForeignKey(DentalService, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        default = 0,
        null = True,
        blank = True,
    )

