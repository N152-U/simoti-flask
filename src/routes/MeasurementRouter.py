from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Measurements import oxygenSaturation, heartRate, temperature

# Models
from models.MeasurementModel import MeasurementModel

main = Blueprint("measurement_blueprint", __name__)


@main.route("/oxygenSaturation")
def get_measurements_oxygen_saturation():
    try:
        measurements_oxygen_saturation = (
            MeasurementModel.get_measurements_oxygen_saturation()
        )
        return jsonify(measurements_oxygen_saturation)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/oxygenSaturation/patient/<patient_id>")
def get_measurements_oxygen_saturation_by_patient(patient_id):
    try:
        measurements_oxygen_saturation = (
            MeasurementModel.get_measurements_oxygen_saturation_by_patient(patient_id)
        )
        if measurements_oxygen_saturation != None:
            return jsonify(measurements_oxygen_saturation)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/oxygenSaturation/add", methods=["POST"])
def get_measurements_oxygen_saturation_add():
    try:
        value = request.json["value"]
        patient_id = request.json["patient_id"]
        oxygen = oxygenSaturation(value, patient_id)
        affected_rows = MeasurementModel.get_measurements_oxygen_saturation_add(oxygen)

        if affected_rows == 1:
            return jsonify({"message": "Success"}), 201
        else:
            return jsonify({"message": "Error on insert"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/heartRate")
def get_measurements_heart_rate():
    try:
        measurements_heart_rate = MeasurementModel.get_measurements_heart_rate()
        return jsonify(measurements_heart_rate)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/heartRate/patient/<patient_id>")
def get_measurements_heart_rate_by_patient(patient_id):
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


@main.route("/heartRate/add", methods=["POST"])
def get_measurements_heart_rate_add():
    try:
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


@main.route("/temperature")
def get_measurements_temperature():
    try:
        measurements_temperature = MeasurementModel.get_measurements_temperature()
        return jsonify(measurements_temperature)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/temperature/patient/<patient_id>")
def get_measurements_temperature_by_patient(patient_id):
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


@main.route("/temperature/add", methods=["POST"])
def get_measurements_temperature_add():
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
