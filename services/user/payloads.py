from faker import Faker

fake = Faker()

class Payloads:

    create_user= \
    {
          "password": fake.password(special_chars=True, digits=True, upper_case=True, lower_case=True), #length=14,
          "login": fake.user_name(),
          "firstName": fake.first_name(),
          "middleName": fake.first_name(),
          "lastName": fake.last_name(),
          "identityNumber": "1234567890"
    }


    change_password = \
        {
            "newPassword": fake.password(special_chars=True, digits=True, upper_case=True, lower_case=True),  # length=14,
        }



    change_info_user= \
        {
            "firstName": fake.first_name(),
            "middleName": fake.first_name(),
            "lastName": fake.last_name(),
            "identityNumber": "1234567890",
            "login": fake.user_name()
        }


