from flask import Blueprint, jsonify, request
import uuid
from werkzeug.security import generate_password_hash as genph
# Entities
from models.entities.Patient import Patient
# Security
from utils.Security import Security

# Models
from models.PatientModel import PatientModel


main = Blueprint("patient_blueprint", __name__)

@main.route("/add", methods=["POST"])
def add_user():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
        
            request_data = request.get_json()
            
            id = uuid.uuid4()
            first_name = request.json["first_name"]
            middle_name = request.json["middle_name"]
            last_name = request.json["last_name"]
            tutor_id = request.json["tutor_id"]
            doctor_id = request.json["doctor_id"]
            date_of_birth = request.json["date_of_birth"]

            newPatient =  Patient(
                str(id), True, first_name, middle_name, last_name, tutor_id, doctor_id, date_of_birth
            )

            affected_rows = PatientModel.add_patient(newPatient)

            if affected_rows == 1:
                return jsonify(newPatient.id),202

            else:
                return jsonify({"message": "Error on insert"}), 500

        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401