from database.db import get_connection
from .entities.Catalog import MunicipalityShape, MunicipalityEdomexShape, TypesOfUsers, Relationship


class CatalogModel:

    @classmethod
    def get_relationships(self):
        try:
            connection = get_connection()
            relationships = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,name, active FROM relationships WHERE active= true ORDER BY id asc"
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    relationship = Relationship(row[0], row[1], row[2])
                    relationships.append(relationship.to_JSON())

            connection.close()
            return relationships
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_municipalities_shape(self):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,name,active,geo_shape FROM municipalities WHERE active= true ORDER BY id asc"
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = MunicipalityShape(row[0], row[1], row[2], row[3])
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_municipalities_edomex_shape(self):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT ogc_fid,name,geo_shape as geometry FROM municipalities_edomex WHERE active= true ORDER BY ogc_fid asc"
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = MunicipalityEdomexShape(row[0], row[1], row[2])
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_types_users(self):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,name,active FROM types_of_users WHERE active= true ORDER BY id asc"
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = TypesOfUsers(row[0], row[1], row[2])
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)
