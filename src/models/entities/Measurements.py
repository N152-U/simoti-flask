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
            "patient_id": self.patient_id,
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
            "patient_id": self.patient_id,
        }


class MeasurementsTemperature:
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


class temperature:
    def __init__(self, value=None, patient_id=None) -> None:
        self.value = value
        self.patient_id = patient_id

    def to_JSON(self):
        return {
            "value": self.value,
            "patient_id": self.patient_id,
        }


class MeasurementsFallDetector:
    def __init__(
        self, id=None, description=None, active: bool = None, created_at=None
    ) -> None:
        self.id = id
        self.description = description
        self.active = active
        self.created_at = created_at

    def to_JSON(self):
        return {
            "id": self.id,
            "description": self.description,
            "active": self.active,
            "created_at": self.created_at,
        }


class FallDetector:
    def __init__(self, description=None, patient_id=None) -> None:
        self.description = description
        self.patient_id = patient_id

    def to_JSON(self):
        return {
            "description": self.description,
            "patient_id": self.patient_id,
        }


class Location:
    def __init__(
        self, patient_id=None, latitude=None, longitude=None, time=None
    ) -> None:
        self.patient_id = patient_id
        self.latitude = latitude
        self.longitude = longitude
        self.time = time

    def to_JSON(self):
        return {
            "patient_id": self.patient_id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "time": self.time,
        }
