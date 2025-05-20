from django.db import models
from .validator import *


GENDER_CHOICES = (
    ('f', 'Female'),
    ('m', 'Masculine'),
    ('n-b', 'Non-binary'),
    ('o', 'Other'),
    ('p', 'Prefer not to say'),
)

class AccountInfo(models.Model):
    name = models.CharField(max_length=32, validators=[validate_username])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200, validators=[validate_password])
    confirmation = models.CharField(max_length=140)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
    birthdate = models.DateField(validators=[validate_birthdate])
    phone = models.CharField(max_length=19, validators=[validate_phone])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name