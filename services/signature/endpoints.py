

HOST = "https://llc-cabinet-api-mwt.csd.ua/api/v1"

class Endpoints:

    get_signature = f"{HOST}/signature-system"
    get_signature_by_id = lambda self, id : f"{HOST}/signature-system/{id}"



