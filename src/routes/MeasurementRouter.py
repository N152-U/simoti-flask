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