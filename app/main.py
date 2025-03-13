from app import create_app, db
from app.routes import api_blueprint

app = create_app()

app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
