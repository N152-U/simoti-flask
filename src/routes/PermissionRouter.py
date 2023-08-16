from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Permission import Permission

# Models
from models.PermissionModel import PermissionModel

main = Blueprint("permission_blueprint", __name__)


@main.route("")
def get_permissions():
    try:
        permissions = PermissionModel.get_permissions()
        return jsonify(permissions)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/<id>")
def get_permission(id):
    try:
        permission = PermissionModel.get_permission(id)
        if permission != None:
            return jsonify(permission)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/add", methods=["POST"])
def add_permission():
    try:
        permission = request.json["permission"]
        description = request.json["description"]
        id = uuid.uuid4()
        newPermission = Permission(str(id), permission, description)

        affected_rows = PermissionModel.add_permission(newPermission)

        if affected_rows == 1:
            return jsonify(newPermission.id)
        else:
            return jsonify({"message": "Error on insert"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/update/<id>", methods=["PUT"])
def update_permission(id):
    try:
        permission = request.json["permission"]
        description = request.json["description"]
        permissionData = Permission(id, permission, description)
     
        affected_rows = PermissionModel.update_permission(permissionData)
        print(affected_rows)
        if affected_rows == 1:
            return jsonify(permissionData.id)
        else:
            return jsonify({"message": "No permission updated"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/delete/<id>", methods=["DELETE"])
def delete_permission(id):
    try:
        permission = Permission(id)

        affected_rows = PermissionModel.delete_permission(permission)

        if affected_rows == 1:
            return jsonify(permission.id)
        else:
            return jsonify({"message": "No permission deleted"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
