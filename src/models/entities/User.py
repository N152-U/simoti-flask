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
