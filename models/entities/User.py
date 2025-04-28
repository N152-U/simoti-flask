from utils.DateFormat import DateFormat


class User:
    def __init__(self, id, username=None, first_name=None, middle_name=None, last_name=None, role=None, active=True) -> None:
        self.id = id
        self.username = username
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.role = role
        self.active = active

    def to_JSON(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstName": self.first_name,
            "middleName": self.middle_name,
            "lastName": self.last_name,
            "roleName": self.role,
            "active": self.active,
        }
class AddUser:
    def __init__(self, id, username=None, first_name=None, middle_name=None, last_name=None, role_id=None, password=None, email=None) -> None:
        self.id = id
        self.username = username
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.role_id = role_id
        self.password = password
        self.email = email

    def to_JSON(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "role_id": self.role_id,
            "password": self.password,
            "email": self.email,
        }

class GetUpdateUser:
    def __init__(self, id, username=None, first_name=None, middle_name=None, last_name=None, role_id=None) -> None:
        self.id = id
        self.username = username
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.role_id = role_id

    def to_JSON(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "role_id": self.role_id,
        }

class UpdateUser:
    def __init__(self, id, username=None, first_name=None, middle_name=None, last_name=None, role_id=None,password=None) -> None:
        self.id = id
        self.username = username
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.role_id = role_id
        self.password = password

    def to_JSON(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "role_id": self.role_id,
            "password": self.password,
        }

class UserValidation:
    def __init__(self, username=None, password=None) -> None:
        self.username = username
        self.password = password

    def to_JSON(self):
        return {
            "username": self.username,
            "firstName": self.password
        }
        
class UserConfirmation:
    def __init__(self, id, username=None, first_name=None, middle_name=None, last_name=None, role_id=None, role=None) -> None:
        self.id = id
        self.username = username
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.role_id = role_id
        self.role = role

    def to_JSON(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstName": self.first_name,
            "middleName": self.middle_name,
            "lastName": self.last_name,
            "roleId": self.role_id,
            "role": self.role,
        }