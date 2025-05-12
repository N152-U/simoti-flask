from flask import Blueprint, jsonify, request
import uuid
from werkzeug.security import generate_password_hash as genph
# Entities

# Security
from utils.Security import Security

# Models

main = Blueprint("patient_blueprint", __name__)

@main.route("/add", methods=["POST"])
def add_user():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
        
            request_data = request.get_json()
            print("request",request_data)

            affected_rows = 1

            if affected_rows == 1:
                #return jsonify(newUser.id)
                return jsonify({"message": "Ok"}), 200

            else:
                return jsonify({"message": "Error on insert"}), 500

        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401