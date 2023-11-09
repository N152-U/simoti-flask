from database.db import get_connection
from .entities.Role import Role
from .entities.Measurements import (
    MeasurementsOxygenSaturation,
    MeasurementsHeartRate,
    MeasurementsTemperature,
)
from datetime import datetime


class MeasurementModel:
    @classmethod
    def get_measurements_oxygen_saturation(self):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,value,active,created_at FROM oxygen_saturation WHERE active= true ORDER BY created_at DESC"
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = MeasurementsOxygenSaturation(
                        row[0], row[1], row[2], row[3]
                    )
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_measurements_oxygen_saturation_by_patient(self, patient_id):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,value,active,created_at FROM oxygen_saturation WHERE active= true AND patient_id = '{0}' ORDER BY created_at DESC".format(
                        patient_id
                    )
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = MeasurementsOxygenSaturation(
                        row[0], row[1], row[2], row[3]
                    )
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_measurements_oxygen_saturation_add(self, oxygen):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO oxygen_saturation (value,patient_id)
                                VALUES (%s,%s)""",
                    (oxygen.value, oxygen.patient_id),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_measurements_heart_rate(self):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,value,active,created_at FROM heart_rate WHERE active= true ORDER BY created_at DESC"
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = MeasurementsHeartRate(row[0], row[1], row[2], row[3])
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_measurements_heart_rate_by_patient(self, patient_id):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,value,active,created_at FROM heart_rate WHERE active= true AND patient_id = '{0}' ORDER BY created_at DESC".format(
                        patient_id
                    )
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = MeasurementsHeartRate(row[0], row[1], row[2], row[3])
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_measurements_heart_rate_add(self, rate):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO heart_rate (value,patient_id)
                                VALUES (%s,%s)""",
                    (rate.value, rate.patient_id),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_measurements_temperature(self):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,value,active,created_at FROM temperature WHERE active= true ORDER BY created_at DESC"
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = MeasurementsTemperature(
                        row[0], row[1], row[2], row[3]
                    )
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_measurements_temperature_by_patient(self, patient_id):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,value,active,created_at FROM temperature WHERE active= true AND patient_id = '{0}' ORDER BY created_at DESC".format(
                        patient_id
                    )
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = MeasurementsTemperature(
                        row[0], row[1], row[2], row[3]
                    )
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_measurements_temperature_add(self, temperatureData):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO temperature (value,patient_id)
                                VALUES (%s,%s)""",
                    (temperatureData.value, temperatureData.patient_id),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
