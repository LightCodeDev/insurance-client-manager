import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "saas_seguros")


TIPOS_SEGURO = ["hogar","auto","vida","medico","robo","decesos","accidentes"]

ESTADOS_PAGO = ["pendiente","pagado","vencido"]