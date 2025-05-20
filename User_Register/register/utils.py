# forbidden passwords
forbidden_passwords = {
    "123456", "123456789", "qwerty", "password", "12345", "12345678",
    "111111", "123123", "1234567890", "000000", "senha", "abc123",
    "1234", "iloveyou", "1q2w3e4r", "qwertyuiop", "admin", "letmein",
    "welcome", "monkey", "dragon", "football", "baseball", "sunshine",
    "princess", "qazwsx", "trustno1", "password1", "123qwe", "zaq12wsx",
    "superman", "ashley", "bailey", "access", "mustang", "shadow",
    "master", "hello", "freedom", "whatever", "!@#$%^&*", "michael",
    "jennifer", "hunter", "jordan", "buster", "soccer", "harley",
    "batman", "thomas", "tigger", "charlie", "maggie", "ginger",
    "joshua", "pepper", "nicole", "daniel", "computer", "michelle",
    "cookie", "summer", "matthew", "george", "cheese", "peppermint",
    "zxcvbnm", "internet", "flower", "andrew", "patrick", "orange",
    "silver", "hannah", "buster123", "pokemon", "starwars", "blink182",
    "abcdef", "asdfgh", "killer", "pepito", "789456", "naruto",
    "pokemon123", "matrix", "love123", "barney", "garfield", "passw0rd",
    "ninja", "123abc", "william", "fuckyou", "sexy", "dallas",
    "batman123", "q1w2e3r4", "jesus", "liverpool", "newyork", "taylor"
}#generic simple passwords**


# token utility
from itsdangerous import URLSafeTimedSerializer
from django.conf import settings

def generate_token(data):
    s = URLSafeTimedSerializer(settings.SECRET_KEY)
    return s.dumps(data)

def verify_token(token):
    s = URLSafeTimedSerializer(settings.SECRET_KEY)
    try:
        return s.loads(token, max_age=3600)
    except:
        return None