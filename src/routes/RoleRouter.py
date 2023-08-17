from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Role import Role

# Models
from models.RoleModel import RoleModel

main = Blueprint("role_blueprint", __name__)


@main.route("")
def get_roles():
    try:
        roles = RoleModel.get_roles()
        return jsonify(roles)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/<id>")
def get_permission(id):
    try:
        permission = RoleModel.get_permission(id)
        if permission != None:
            return jsonify(permission)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/add", methods=["POST"])
def add_role():
    try:
        permissions = request.json["permissions"]
        role = request.json["role"]
        id = uuid.uuid4()
        newPermission = Role(str(id), role, permissions)

        affected_rows = RoleModel.add_role(newPermission)

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
        permissionData = Role(id, permission, description)

        affected_rows = RoleModel.update_permission(permissionData)
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
        permission = Role(id)

        affected_rows = RoleModel.delete_permission(permission)

        if affected_rows == 1:
            return jsonify(permission.id)
        else:
            return jsonify({"message": "No permission deleted"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
