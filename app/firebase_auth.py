import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load FIREBASE_CREDENTIALS from environment variable
firebase_credentials_path = os.getenv("FIREBASE_CREDENTIALS")

if not firebase_credentials_path:
    raise ValueError("FIREBASE_CREDENTIALS environment variable is not set or is empty")

# Initialize Firebase
cred = credentials.Certificate(firebase_credentials_path)
firebase_admin.initialize_app(cred)

def verify_firebase_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token  # Contains UID, email, name, etc.
    except Exception as e:
        return None