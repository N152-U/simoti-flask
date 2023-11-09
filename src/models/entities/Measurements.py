class MeasurementsOxygenSaturation:
    def __init__(
        self, id=None, value=None, active: bool = None, created_at=None
    ) -> None:
        self.id = id
        self.value = value
        self.active = active
        self.created_at = created_at

    def to_JSON(self):
        return {
            "id": self.id,
            "value": self.value,
            "active": self.active,
            "created_at": self.created_at,
        }
