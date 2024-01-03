from utils.DateFormat import DateFormat


class Permission:
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
class PermissionList:
    def __init__(self, permission=None) -> None:
        self.permission = permission
    def to_JSON(self):
        return self.permission

