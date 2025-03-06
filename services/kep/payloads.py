from faker import Faker

fake = Faker()

class Payloads:

    create_kep_verify= \
        {
            "data": "string",
            "signature": "string"
        }
    print(create_kep_verify)

    create_kep_generate_hash = "aaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(create_kep_generate_hash)


