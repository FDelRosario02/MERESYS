from django.db import models

# Create your models here.
class Patient(models.Model):
    # The date and time when the patient was created.
    created_at = models.DateTimeField(auto_now_add=True)
    # The first name of the patient.
    first_name = models.CharField(max_length=50)
    # The last name of the patient.
    last_name = models.CharField(max_length=50)
    # The date of birth of the patient.
    date_of_birth = models.DateField(null=True, blank=True)
    # The gender of the patient.
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], blank=True)
    # The address of the patient.
    address = models.CharField(max_length=200, blank=True)
    # The phone number of the patient.
    phone = models.CharField(max_length=12, blank=True)
    # The email address of the patient.
    email = models.EmailField(blank=True)
    # The blood type of the patient.
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_type = models.CharField(max_length=5, choices=BLOOD_TYPE_CHOICES, blank=True)
    # Any allergies the patient may have.
    allergies = models.TextField(blank=True)

    # Enfermedad del paciente
    disease = models.CharField(max_length=100, blank=True)

    # Síntomas del paciente
    symptoms = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"