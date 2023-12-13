class MunicipalityShape:
    def __init__(self, id=None, name=None, active: bool = None, geo_shape=None) -> None:
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


class MunicipalityEdomexShape:
    def __init__(self, ogc_fid=None, name=None, geo_shape=None) -> None:
        self.ogc_fid = ogc_fid
        self.name = name
        self.geo_shape = geo_shape['coordinates'][0]

    def to_JSON(self):
        return {
            "geometry": {
                "coordinates": self.geo_shape,
                "type": "polygon",
            },
            "properties": {"name": self.name, "ObjectID": self.ogc_fid},
            "type": "Feature",
        }
