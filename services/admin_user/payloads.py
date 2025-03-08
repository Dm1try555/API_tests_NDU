from faker import Faker

fake = Faker()

class Payloads:

    create_user_from_admin= \
    {
          "password": fake.password(special_chars=True, digits=True, upper_case=True, lower_case=True), #length=14,
          "login": fake.user_name(),
          "firstName": fake.first_name(),
          "lastName": fake.last_name(),
          "rolesId": [
            6
          ]
    }
    print(create_user_from_admin)


    change_password = \
        {
            "newPassword": fake.password(special_chars=True, digits=True, upper_case=True, lower_case=True),  # length=14,

        }
    print(change_password)

    change_info_user_from_admin = \
        {
            "firstName": fake.first_name(),
            "middleName": fake.first_name(),
            "lastName": fake.last_name(),
            "identityNumber": fake.ssn(),
            "login": fake.user_name()
        }
    print(change_info_user_from_admin)


