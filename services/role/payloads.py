from faker import Faker

fake = Faker()

class Payloads:

    create_new_role= \
        {
            "role": {
                "name": fake.job(),
                "description": fake.sentence(),
                "dependCodes": [
                    fake.uuid4()
                ],
                "isAdminPart": fake.boolean()
            },
            "grantedPermissionNames": [
                fake.word()
            ]
        }
    print(create_new_role)

    change_role = \
        {
            "role": {
                "name": fake.job(),
                "description": fake.sentence(),
                "dependCodes": [
                    fake.uuid4()
                ],
                "isAdminPart": fake.boolean()
            },
            "grantedPermissionNames": [
                fake.word()
            ]
        }



