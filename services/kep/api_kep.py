import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import pkcs12, Encoding
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

        with open("tests/files/physician/Key-6.pfx", "rb") as f:
            pfx_data = f.read()

        self.private_key, self.cert, self.additional_cert = pkcs12.load_key_and_certificates(
            pfx_data,
            b"1234qwer",
            backend=default_backend()
        )
        self.encode_cert = base64.b64encode(
            self.cert.public_bytes(encoding=Encoding.DER)
        ).decode()
        self.encode_cert_serial = format(self.cert.serial_number, 'x').upper()

    @allure.step("Create KEP integration")
    def create_kep_integration(self):
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4ODg4ODg4ODg4IiwianRpIjoiZjZhZWUxYWEtYzAwYi00ZDIxLTg1NDctM2ViMjUxNDdlODZhIiwidWlkIjoiOCIsImlwIjoiaXBBZGRyZXNzIiwiZXhwIjoxNzUyNjcyMzQ2LCJpc3MiOiJDb3JlSWRlbnRpdHkiLCJhdWQiOiJDb3JlSWRlbnRpdHlVc2VyIn0.YgF5iZRVcdXulLZQ7DQybGwT0eqsikpmCIq2mh7WyiA"

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
