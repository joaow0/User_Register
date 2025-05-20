from django.core.exceptions import ValidationError
import re



def validate_username(value):
    from register.models import AccountInfo
    if len(value) < 3:
        raise ValidationError('The username must be at least 3 characters long.')

    if AccountInfo.objects.filter(name=value).exists():
        raise ValidationError('This username already exists. Try another one.')

    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', value):
        raise ValidationError('The username cannot contain special characters.')

    if value == value[0] * len(value):
        # if the username is composed entirely of the same character
        raise ValidationError('The username cannot be composed of only one repeated character. Try again.')



def validate_password(value):
    from register.utils import forbidden_passwords
    if len(value) < 8:
        raise ValidationError('The password must be at least 8 characters long.')

    if value == value[0] * len(value):
        raise ValidationError('The password cannot consist of only one repeated character.')

    if not re.fullmatch(r"^[A-Za-z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?`~]+$", value) or value in forbidden_passwords:
        raise ValidationError('Weak password, please try again.')



def validate_birthdate(value):
    from datetime import date
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 14:
        raise ValidationError('You must be at least 14 years old to register.')




def validate_phone(value):
    from register.models import AccountInfo
    if len(value) < 12 or not re.fullmatch(r'^\+?\d{10,15}$', value):
        raise ValidationError('Invalid phone number. Please try again.')

    if AccountInfo.objects.filter(phone=value).exists():
        raise ValidationError('The phone number is already in use.')
