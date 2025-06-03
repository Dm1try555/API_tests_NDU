import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")


class Endpoints:

    get_printed_forms = f"{HOST}/printed-forms"
    create_printed_forms = lambda self, id: f"{HOST}/printed-forms/{id}"
    get_view_by_id = lambda self, id: f"{HOST}/printed-forms/{id}/view"
    get_printed_forms_type = lambda self, type_id: f"{HOST}/printed-forms/type/{type_id}"
    get_printed_forms_placeholder = f"{HOST}/printed-forms/placeholder"



