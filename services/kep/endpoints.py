import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:

    get_kep_integration = f"{HOST}/kep/integration"
    get_kep_generate = f"{HOST}/kep/generate"
    create_kep_verify = f"{HOST}/kep/verify"
    create_kep_verify_hash = f"{HOST}/kep/verify/hash"
    create_kep_generate_hash = f"{HOST}/kep/generate/hash"








