from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Measurements import (
    oxygenSaturation,
    heartRate,
    temperature,
    FallDetector,
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


@main.route("/oxygenSaturation/patient/<patient_id>")
def get_measurements_oxygen_saturation_by_patient(patient_id):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_oxygen_saturation = (
                MeasurementModel.get_measurements_oxygen_saturation_by_patient(
                    patient_id
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


@main.route("/heartRate/patient/<patient_id>")
def get_measurements_heart_rate_by_patient(patient_id):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_oxygen_saturation = (
                MeasurementModel.get_measurements_heart_rate_by_patient(patient_id)
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
        print('request',request.json["value"],request.json["patient_id"])
        value = request.json["value"]
        patient_id = request.json["patient_id"]
        rate = heartRate(value, patient_id)
        affected_rows = MeasurementModel.get_measurements_heart_rate_add(rate)

        if affected_rows == 1:
            return jsonify({"message": "Success"}), 201
        else:
            return jsonify({"message": "Error on insert"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
'''     else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401 '''


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


@main.route("/temperature/patient/<patient_id>")
def get_measurements_temperature_by_patient(patient_id):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_temperature = (
                MeasurementModel.get_measurements_temperature_by_patient(patient_id)
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


@main.route("/fallDetector/patient/<patient_id>")
def get_measurements_fall_detector_by_patient(patient_id):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            measurements_fall_detector = (
                MeasurementModel.get_measurements_fall_detector_by_patient(patient_id)
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


@main.route("/location/<startDate>/<finalDate>")
def get_locations_by_date(startDate, finalDate):
    has_access = Security.verify_token(request.headers)
    # if has_access:
    try:
        locations = MeasurementModel.get_locations_by_date(startDate, finalDate)
        if locations != None:
            return jsonify({"features": locations, "type": "FeatureCollection"})
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    # else:
    #   response = jsonify({"message": "Unauthorized"})
    # return response, 401
