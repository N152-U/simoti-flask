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


class oxygenSaturation:
    def __init__(self, value=None, patient_id=None) -> None:
        self.value = value
        self.patient_id = patient_id

    def to_JSON(self):
        return {
            "value": self.value,
            "active": self.patient_id,
        }

class MeasurementsHeartRate:
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

class heartRate:
    def __init__(self, value=None, patient_id=None) -> None:
        self.value = value
        self.patient_id = patient_id

    def to_JSON(self):
        return {
            "value": self.value,
            "active": self.patient_id,
        }