from flask import Blueprint, jsonify, request
import uuid

# Entities

# Models
from models.MeasurementModel import MeasurementModel

main = Blueprint("measurement_blueprint", __name__)


@main.route("/oxygenSaturation")
def get_measurements_oxygen_saturation():
    try:
        measurements_oxygen_saturation = MeasurementModel.get_measurements_oxygen_saturation()
        return jsonify(measurements_oxygen_saturation)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    
@main.route("/oxygenSaturation/patient/<patient_id>")
def get_measurements_oxygen_saturation_by_patient(patient_id):
    try:
        measurements_oxygen_saturation = MeasurementModel.get_measurements_oxygen_saturation_by_patient(patient_id)
        if measurements_oxygen_saturation != None:
            return jsonify(measurements_oxygen_saturation)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500