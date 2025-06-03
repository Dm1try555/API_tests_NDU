import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.backends import default_backend
import requests
import allure
from config.headers import Headers
from utils.helper import Helper
from services.kep.endpoints import Endpoints
import os


class KepAPI(Helper):
    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        
        # Загрузка PFX и инициализация ключей/сертификатов
        with open("tests/files/physician/Key-6.pfx", "rb") as f:
            pfx_data = f.read()

        self.private_key, self.cert, self.additional_cert = pkcs12.load_key_and_certificates(
            pfx_data,
            b"1234qwer",
            backend=default_backend()
        )
        self.encode_cert = base64.b64encode(self.cert.public_bytes()).decode()
        self.encode_cert_serial = format(self.cert.serial_number, 'x').upper()

    @allure.step("Create KEP integration")
    def create_kep_integration(self):
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxNDEyNDUiLCJqdGkiOiJkOGY3NDQ0Mi0wZTQyLTQ1OWItOTU1Ny00OTE3NmNjMmJkYzYiLCJ1aWQiOiIyIiwiaXAiOiJpcEFkZHJlc3MiLCJleHAiOjE3NDc0OTA4NDcsImlzcyI6IkNvcmVJZGVudGl0eSIsImF1ZCI6IkNvcmVJZGVudGl0eVVzZXIifQ.P6UEkZ9J7nG3aX5qElZOVp-d_CVukQBB_HifprNjRTo"

        message = token.encode()

        signature = self.private_key.sign(
            data=message,
            padding=padding.PKCS1v15(),
            algorithm=hashes.SHA256()
        )
        signature_b64 = base64.b64encode(signature).decode()

        payload = {
            "encodeCert": self.encode_cert,
            "encodeCertSerial": self.encode_cert_serial,
            "token": token,
            "signature": signature_b64
        }

        response = requests.post(
            url=self.endpoints.create_kep_integration,
            headers=self.headers.basic,
            json=payload
        )

        assert response.status_code == 200, response.json()
        return response.json()
