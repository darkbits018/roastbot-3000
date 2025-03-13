from app import create_app, db
from app.models import User  # Import models to register them

app = create_app()

# Run inside application context
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
