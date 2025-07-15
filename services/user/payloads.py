from faker import Faker
import uuid

fake = Faker()

class Payloads:

    create_user = {
        "password": "Test1234!",
        "login": f"{fake.user_name()}_{uuid.uuid4().hex[:8]}", 
        "firstName": fake.first_name(),
        "middleName": fake.first_name(),
        "lastName": fake.last_name(),
        "identityNumber": "1234567890"
    }

    change_password = {
        "newPassword": "NewPass123!"
    }

    change_info_user = {
        "firstName": fake.first_name(),
        "middleName": fake.first_name(),
        "lastName": fake.last_name(),
        "identityNumber": "1234567890",
        "login": fake.user_name()
    }
