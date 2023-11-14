class MunicipalityShape:
    def __init__(
        self, id=None, name=None, active: bool = None, geo_shape=None
    ) -> None:
        self.id = id
        self.name = name
        self.active = active
        self.geo_shape = geo_shape

    def to_JSON(self):
        return {
            "id": self.id,
            "municipality": self.name,
            "active": self.active,
            "geo_shape": self.geo_shape,
        }