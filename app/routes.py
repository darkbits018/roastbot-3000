from firebase_admin import auth
from flask import Blueprint, request, jsonify

from app.roast_service import generate_roast
from app import db
from app.models import User

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/login", methods=["POST"])
def login():
    data = request.json
    id_token = data.get("idToken")

    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token["uid"]
        name = decoded_token.get("name", "Unknown User")
        email = decoded_token.get("email", "No Email")

        # Check if user exists in PostgreSQL
        user = User.query.filter_by(uid=uid).first()
        if not user:
            new_user = User(uid=uid, name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

        return jsonify({"message": "Login successful", "uid": uid, "name": name, "email": email})

    except Exception as e:
        return jsonify({"error": str(e)}), 401



@api_blueprint.route("/roast", methods=["POST"])
def roast():
    data = request.json
    user_message = data.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    roast_response = generate_roast(user_message)
    return jsonify({"roast": roast_response})
