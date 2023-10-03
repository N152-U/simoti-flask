class RoleAll:
    def __init__(self, id=None, role=None, permissions=None, active=True) -> None:
        self.id = id
        self.role = role
        self.active = active

    def to_JSON(self):
        return {
            "id": self.id,
            "role": self.role,
            "active": self.active
        }
