from faker import Faker

fake = Faker()

class Payloads:

    create_account = {
        "phoneNumber": fake.numerify("+380#########"),
        "email": fake.email(),
        "isNotifyEmail": True or False,
        "language": "UA"
    }

