import os
import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials

load_dotenv()

# Load Firebase credentials
firebase_cred_path = os.getenv("FIREBASE_CREDENTIALS")
if firebase_cred_path:
    cred = credentials.Certificate(firebase_cred_path)
    firebase_admin.initialize_app(cred)

# Database configuration (used in `__init__.py`)
DATABASE_URL = os.getenv("DATABASE_URL")
