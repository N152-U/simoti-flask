from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Role import Role

# Models
from models.RoleModel import RoleModel

# Security
from utils.Security import Security

main = Blueprint("role_blueprint", __name__)


@main.route("")
def get_roles():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            roles = RoleModel.get_roles()
            return jsonify(roles)
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

@main.route("/<id>")
def get_role(id):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            role = RoleModel.get_role(id)
            if role != None:
                return jsonify(role)
            else:
                return jsonify({}), 404
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

@main.route("/getUpdate/<id>")
def get_update_role(id):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            role = RoleModel.get_update_role(id)
            lista_con_elementos = []
            for permission in role["permissions"]:
                lista_con_elementos.append(permission["id"])
            role["permissions"] = lista_con_elementos
            if role != None:
                return jsonify(role)
            else:
                return jsonify({}), 404
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

@main.route("/add", methods=["POST"])
def add_role():
    has_access = Security.verify_token(request.headers)
    if has_access:
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
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

@main.route("/update/<id>", methods=["PUT"])
def update_role(id):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            permissions = request.json["permissions"]
            role = request.json["role"]
            permissionData = Role(id, role, permissions)

            RoleModel.delete_role_by_id(permissionData)
            affected_rows = RoleModel.update_role(permissionData)
            print(affected_rows)
            if affected_rows == 1:
                return jsonify(permissionData.id)
            else:
                return jsonify({"message": "No role updated"}), 404

        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

@main.route("/delete/<id>", methods=["DELETE"])
def delete_role(id):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            role = Role(id)
            affected_rows = RoleModel.delete_role(role)

            if affected_rows == 1:
                return jsonify(role.id)
            else:
                return jsonify({"message": "No role deleted"}), 404

        except Exception as ex:
            return jsonify({"message": str(ex)}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401