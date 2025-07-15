import random
import string
from faker import Faker

fake = Faker()

def generate_strong_password(length=14):
    
    if length < 4:
        raise ValueError ("Password length must be at least 4 characters")

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?"),
    ]

    
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

class Payloads:
    create_user_from_admin = {
        "password": generate_strong_password(),
        "login": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "rolesId": [1]
    }

    change_password = {
        "newPassword": generate_strong_password()
    }

    change_info_user_from_admin = {
        "firstName": fake.first_name(),
        "middleName": fake.first_name(),
        "lastName": fake.last_name(),
        "identityNumber": fake.ssn(),
        "login": fake.user_name()
    }
