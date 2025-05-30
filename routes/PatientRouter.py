from flask import Blueprint, jsonify, request
import uuid
from werkzeug.security import generate_password_hash as genph
# Entities
from models.entities.Patient import Patient, PatientGeneralStatus, PatientHabitsAndBackgroud
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
            
            patient_id=id
            general_condition=int(request.json["estadoGeneral"])
            energy=int(request.json["energia"])
            fever=int(request.json["fiebre"])
            chest_pain=int(request.json["dolorPecho"])
            dizziness=int(request.json["mareos"])
            high_temperature=int(request.json["tempAlta"])
            sweating=int(request.json["sudores"])
            palpitations=int(request.json["palpitaciones"])
            resting_tachycardia=int(request.json["taquicardiaReposo"])
            falls=int(request.json["caidas"])
            instability=int(request.json["inestabilidad"])
            change_of_location=int(request.json["cambioLugar"])
            exercise_difficulty=int(request.json["dificultadEjercicio"])
            dyspnea_activities=int(request.json["disneaActividades"])
            
            fruits_vegetables = int(request.json["frutasVerduras"])
            water = int(request.json["agua"])
            physical_activity = int(request.json["actividadFisica"])
            sleep_hours = int(request.json["horasSueño"])
            nighttime_waking = int(request.json["despertarNocturno"])
            medical_history = int(request.json["historiaMedica"])
            medications = int(request.json["medicamentos"])
            cardiac_history = int(request.json["antecedentesCardiacos"])
            respiratory_history = int(request.json["antecedentesRespiratorios"])
            obesity = int(request.json["obesidad"])
            family_diabetes = ("No" if request.json["diabetesFamilia"] == "0" else request.json["diabetesFamilia"])
            diabetes = ("No" if request.json["diabetes"] == "0" else request.json["diabetes"])
            chronic_disease = int(request.json["enfermedadCronica"])
            disease_details = ("No" if request.json["cualEnfermedad"] == "0" else request.json["cualEnfermedad"])

            newPatient =  Patient(
                str(id), True, first_name, middle_name, last_name, tutor_id, doctor_id, date_of_birth
            )
            
            newPatientGeneralStatus = PatientGeneralStatus(patient_id, general_condition, energy, fever, chest_pain, dizziness, high_temperature, sweating, 
                 palpitations, resting_tachycardia, falls, instability, change_of_location, exercise_difficulty, dyspnea_activities)
            
            newPatientHabitsAndBackgroud = PatientHabitsAndBackgroud(patient_id, fruits_vegetables, water, physical_activity, sleep_hours, nighttime_waking, medical_history, medications, 
                                                                     cardiac_history, respiratory_history, obesity, family_diabetes, diabetes, chronic_disease, disease_details)

            print("newPatientHabitsAndBackgroud",newPatientHabitsAndBackgroud)

            affected_rows = PatientModel.add_patient(newPatient,newPatientGeneralStatus,newPatientHabitsAndBackgroud)

            if affected_rows == 1:
                return jsonify(newPatient.id),201

            else:
                return jsonify({"message": "Error on insert"}), 500

        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401
    
    
@main.route("")
def get_patients():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            patients = PatientModel.get_patients()
            return jsonify(patients)
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401