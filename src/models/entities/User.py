from utils.DateFormat import DateFormat


class User:
    def __init__(self, id, permission=None, description=None, active=True) -> None:
        self.id = id
        self.permission = permission
        self.description = description
        self.active = active

    def to_JSON(self):
        return {
            "id": self.id,
            "permission": self.permission,
            "description": self.description,
            "active": self.active,
        }
