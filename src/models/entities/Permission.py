from utils.DateFormat import DateFormat


class Permission:
    def __init__(self, id, permission=None, description=None) -> None:
        self.id = id
        self.permission = permission
        self.description = description

    def to_JSON(self):
        return {
            "id": self.id,
            "permission": self.permission,
            "description": self.description,
        }
