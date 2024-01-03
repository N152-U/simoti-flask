from flask import Blueprint, jsonify, request
# Models
from models.CatalogModel import CatalogModel
# Security
from utils.Security import Security


main = Blueprint("catalog_blueprint", __name__)


@main.route("/municipalities/shapes")
def get_municipalities_shape():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            shapes = (
                CatalogModel.get_municipalities_shape()
            )
            return jsonify(shapes)
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

@main.route("/municipalities/edomex/shapes")
def get_municipalities_edomex_shape():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            shapes = (
                CatalogModel.get_municipalities_edomex_shape()
            )
            return jsonify(shapes)
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401
