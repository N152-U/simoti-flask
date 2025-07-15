from flask import Blueprint, jsonify, request
import uuid
import firebase_admin
from firebase_admin import credentials, messaging
from datetime import datetime

# Entities
from models.entities.Measurements import (
    WearableAdd,
    oxygenSaturation,
    heartRate,
    temperature,
    FallDetector,
    LocationAdd
)

# Models
from models.MeasurementModel import MeasurementModel

# Security
from utils.Security import Security


main = Blueprint("measurement_blueprint", __name__)


@main.route("/oxygenSaturation")
def get_measurements_oxygen_saturation():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_oxygen_saturation = (
                MeasurementModel.get_measurements_oxygen_saturation()
            )
            return jsonify(measurements_oxygen_saturation)
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401


@main.route("/oxygenSaturation/patient/<patient_id>/<initial_date>/<end_date>")
def get_measurements_oxygen_saturation_by_patient(patient_id,initial_date,end_date):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_oxygen_saturation = (
                MeasurementModel.get_measurements_oxygen_saturation_by_patient(
                    patient_id,initial_date,end_date
                )
            )
            if measurements_oxygen_saturation != None:
                return jsonify(measurements_oxygen_saturation)
            else:
                return jsonify({}), 404
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401


@main.route("/oxygenSaturation/add", methods=["POST"])
def get_measurements_oxygen_saturation_add():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            value = request.json["value"]
            patient_id = request.json["patient_id"]
            oxygen = oxygenSaturation(value, patient_id)
            affected_rows = MeasurementModel.get_measurements_oxygen_saturation_add(
                oxygen
            )

            if affected_rows == 1:
                if value < 88:
                    device_token = MeasurementModel.get_token_tutor(patient_id)

                    if device_token:
                        message = messaging.Message(
                            notification=messaging.Notification(
                                title="Alerta: Saturación de oxígeno fuera de lo normal",
                                body=f"La saturación de oxígeno registrada es {value}%. Favor de verificar al paciente."
                            ),
                            token=device_token
                        )

                        try:
                            response = messaging.send(message)
                            print(f"Notificación enviada: {response}")
                        except Exception as e:
                            print(f"Error al enviar la notificación: {str(e)}")                
                return jsonify({"message": "Success"}), 201
            else:
                return jsonify({"message": "Error on insert"}), 500

        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401
    
@main.route("/location/add", methods=["POST"])
def get_measurements_location_add():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            latitude = request.json["latitude"]
            longitude = request.json["longitude"]
            patient_id = request.json["patient_id"]
            location = LocationAdd(latitude, longitude, patient_id)
            affected_rows = MeasurementModel.get_measurements_location_add(
                location
            )

            if affected_rows == 1:
                return jsonify({"message": "Success"}), 201
            else:
                return jsonify({"message": "Error on insert"}), 500

        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401


@main.route("/heartRate")
def get_measurements_heart_rate():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_heart_rate = MeasurementModel.get_measurements_heart_rate()
            return jsonify(measurements_heart_rate)
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401


@main.route("/heartRate/patient/<patient_id>/<initial_date>/<end_date>")
def get_measurements_heart_rate_by_patient(patient_id,initial_date,end_date):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_oxygen_saturation = (
                MeasurementModel.get_measurements_heart_rate_by_patient(patient_id,initial_date,end_date)
            )
            if measurements_oxygen_saturation != None:
                return jsonify(measurements_oxygen_saturation)
            else:
                return jsonify({}), 404
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401

@main.route("/heartRate/add", methods=["POST"])
def get_measurements_heart_rate_add():
    try:
        value = request.json["value"]
        patient_id = request.json["patient_id"]
        rate = heartRate(value, patient_id)
        affected_rows = MeasurementModel.get_measurements_heart_rate_add(rate)

        if affected_rows == 1:
            
            if value < 66 or value > 100:
                device_token = MeasurementModel.get_token_tutor(patient_id)

                if device_token:
                    message = messaging.Message(
                        notification=messaging.Notification(
                            title="Alerta: Frecuencia cardíaca fuera de lo normal",
                            body=f"La frecuencia cardíaca registrada es {value} bpm. Favor de verificar al paciente."
                        ),
                        token=device_token
                    )

                    try:
                        response = messaging.send(message)
                        print(f"Notificación enviada: {response}")
                    except Exception as e:
                        print(f"Error al enviar la notificación: {str(e)}")

            return jsonify({"message": "Success"}), 201
        else:
            return jsonify({"message": "Error on insert"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401



@main.route("/temperature")
def get_measurements_temperature():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_temperature = MeasurementModel.get_measurements_temperature()
            return jsonify(measurements_temperature)
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401


@main.route("/temperature/patient/<patient_id>/<initial_date>/<end_date>")
def get_measurements_temperature_by_patient(patient_id,initial_date,end_date):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_temperature = (
                MeasurementModel.get_measurements_temperature_by_patient(patient_id,initial_date,end_date)
            )
            if measurements_temperature != None:
                return jsonify(measurements_temperature)
            else:
                return jsonify({}), 404
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401


@main.route("/temperature/add", methods=["POST"])
def get_measurements_temperature_add():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            value = request.json["value"]
            patient_id = request.json["patient_id"]
            temperatureData = temperature(value, patient_id)
            affected_rows = MeasurementModel.get_measurements_temperature_add(
                temperatureData
            )

            if affected_rows == 1:
                return jsonify({"message": "Success"}), 201
            else:
                return jsonify({"message": "Error on insert"}), 500

        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401


@main.route("/fallDetector")
def get_measurements_fall_detector():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_fall_detector = (
                MeasurementModel.get_measurements_fall_detector()
            )
            return jsonify(measurements_fall_detector)
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401


@main.route("/fallDetector/patient/<patient_id>/<initial_date>/<end_date>")
def get_measurements_fall_detector_by_patient(patient_id,initial_date,end_date):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_fall_detector = (
                MeasurementModel.get_measurements_fall_detector_by_patient(patient_id,initial_date,end_date)
            )
            if measurements_fall_detector != None:
                return jsonify(measurements_fall_detector)
            else:
                return jsonify({}), 404
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401


@main.route("/fallDetector/add", methods=["POST"])
def get_measurements_fall_detector_add():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            description = request.json["description"]
            patient_id = request.json["patient_id"]
            fallDetectorData = FallDetector(description, patient_id)
            affected_rows = MeasurementModel.get_measurements_fall_detector_add(
                fallDetectorData
            )

            if affected_rows == 1:
                return jsonify({"message": "Success"}), 201
            else:
                return jsonify({"message": "Error on insert"}), 500

        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401

@main.route("/location/patient/<patient_id>/<initial_date>/<end_date>")
def get_measurements_location_by_patient(patient_id,initial_date,end_date):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_location= (
                MeasurementModel.get_measurements_location_by_patient(patient_id,initial_date,end_date)
            )
            if measurements_location != None:
                return jsonify(measurements_location)
            else:
                return jsonify({}), 404
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401
    
@main.route("/location/<startDate>/<finalDate>")
def get_locations_by_date(startDate, finalDate):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            locations = MeasurementModel.get_locations_by_date(startDate, finalDate)
            if locations != None:
                return jsonify({"features": locations, "type": "FeatureCollection"})
            else:
                return jsonify({}), 404
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
      response = jsonify({"message": "Unauthorized"})
    return response, 401

@main.route('/send-alert', methods=['POST'])
def send_push_notification():
    data = request.json
    #obtener token de la BD
    device_token = data.get("token")  # El FCM token del dispositivo
    title = data.get("title", "Alerta médica")
    body = data.get("body", "El paciente ha superado los límites de temperatura.")
    
    if not device_token:
        return jsonify({"error": "Token del dispositivo requerido"}), 400

    # Crear el mensaje
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=device_token
    )

    try:
        response = messaging.send(message)
        print(response)

        return jsonify({"message": "Notificación enviada", "response_id": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main.route("/add/<patient_id>/", methods=["POST"])
def measurements_automatic_add(patient_id):
    try:
        
        affected_rows = MeasurementModel.measurements_automatic_add(
            patient_id
        )
        
        if affected_rows['success'] == True:
            return jsonify(affected_rows), 201
        else:
            return jsonify({"message": "Error on insert"}), 500
        return jsonify({"message": "Success"}), 201
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    
@main.route("/addWearable/<patient_id>/", methods=["POST"])
def measurements_wearable_add(patient_id):
    try:
        pulso = request.json["pulso"]
        temperatura = request.json["temperatura"]
        spo2 = request.json["spo2"]
        latitude = request.json["latitude"]
        longitude = request.json["longitude"]
        patient_id = patient_id
        add = WearableAdd(pulso, temperatura, spo2, latitude, longitude, patient_id)
        affected_rows = MeasurementModel.measurements_wearable_add(add)
        
        if affected_rows == 1:
            
            device_token = MeasurementModel.get_token_tutor(patient_id)
            
            if pulso < 66 or pulso > 100:
                
                if device_token:
                    message = messaging.Message(
                        notification=messaging.Notification(
                            title="Alerta: Frecuencia cardíaca fuera de lo normal",
                            body=f"La frecuencia cardíaca registrada es {pulso} bpm. Favor de verificar al paciente."
                        ),
                        token=device_token
                    )

                    try:
                        response = messaging.send(message)
                        print(f"Notificación enviada: {response}")
                    except Exception as e:
                        print(f"Error al enviar la notificación: {str(e)}")
                        
            if spo2 < 88:

                    if device_token:
                        messageOx = messaging.Message(
                            notification=messaging.Notification(
                                title="Alerta: Saturación de oxígeno fuera de lo normal",
                                body=f"La saturación de oxígeno registrada es del {spo2}%. Favor de verificar al paciente."
                            ),
                            token=device_token
                        )

                        try:
                            response = messaging.send(messageOx)
                            print(f"Notificación enviada: {response}")
                        except Exception as e:
                            print(f"Error al enviar la notificación: {str(e)}")  

            return jsonify({"message": "Success"}), 201
        else:
            return jsonify({"message": "Error on insert"}), 500
        #return jsonify(affected_rows), 201 if affected_rows.get("success") else 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
