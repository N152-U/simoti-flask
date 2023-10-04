from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.User import User, AddUser, UpdateUser

# Models
from models.UserModel import UserModel

main = Blueprint("user_blueprint", __name__)


@main.route("")
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/<id>")
def get_user(id):
    try:
        user = UserModel.get_user(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/add", methods=["POST"])
def add_user():
    try:
        role_id = request.json["role_id"]
        username = request.json["username"]
        first_name = request.json["first_name"]
        middle_name = request.json["middle_name"]
        last_name = request.json["last_name"]
        password = request.json["password"]
        id = uuid.uuid4()
        newUser = AddUser(
            str(id), username, first_name, middle_name, last_name, role_id, password
        )

        affected_rows = UserModel.add_user(newUser)

        if affected_rows == 1:
            return jsonify(newUser.id)
        else:
            return jsonify({"message": "Error on insert"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/getUpdate/<id>")
def get_user_update(id):
    try:
        user = UserModel.get_user_update(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/update/<id>", methods=["PUT"])
def update_user(id):
    try:
        role_id = request.json["role_id"]
        username = request.json["username"]
        first_name = request.json["first_name"]
        middle_name = request.json["middle_name"]
        last_name = request.json["last_name"]
        password = request.json["password"]

        updateUser = UpdateUser(
            str(id), username, first_name, middle_name, last_name, role_id, password
        )

        affected_rows = UserModel.update_user(updateUser)

        if affected_rows == 1:
            return jsonify(updateUser.id)
        else:
            return jsonify({"message": "No user updated"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/delete/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        user = User(id)

        affected_rows = UserModel.delete_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({"message": "No user deleted"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
