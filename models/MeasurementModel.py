from database.db import get_connection
from .entities.Role import Role
from .entities.Measurements import (
    MeasurementsOxygenSaturation,
    MeasurementsHeartRate,
    MeasurementsTemperature,
    MeasurementsFallDetector,
    Location,
    LocationPatient
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
    def get_measurements_oxygen_saturation_by_patient(self, patient_id,initial_date,end_date):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,value,active,created_at FROM oxygen_saturation WHERE active= true AND patient_id = '{0}' AND created_at BETWEEN '{1} 00:00:00' AND '{2} 23:59:59' ORDER BY created_at DESC".format(
                        patient_id,initial_date,end_date
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
    def get_measurements_location_add(self, location):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO location (latitude,longitude,patient_id)
                                VALUES (%s,%s,%s)""",
                    (location.latitude, location.longitude, location.patient_id),
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
    def get_measurements_heart_rate_by_patient(self, patient_id,initial_date,end_date):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,value,active,created_at FROM heart_rate WHERE active= true AND patient_id = '{0}' AND created_at BETWEEN '{1} 00:00:00' AND '{2} 23:59:59' ORDER BY created_at DESC".format(
                        patient_id,initial_date,end_date
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
    def get_measurements_temperature_by_patient(self, patient_id,initial_date,end_date):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,value,active,created_at FROM temperature WHERE active= true AND patient_id = '{0}' AND created_at BETWEEN '{1} 00:00:00' AND '{2} 23:59:59' ORDER BY created_at DESC".format(
                        patient_id,initial_date,end_date
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

    @classmethod
    def get_measurements_fall_detector(self):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,description,active,created_at FROM fall_detector WHERE active= true ORDER BY created_at DESC"
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = MeasurementsFallDetector(
                        row[0], row[1], row[2], row[3]
                    )
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_measurements_fall_detector_by_patient(self, patient_id,initial_date,end_date):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,description,active,created_at FROM fall_detector WHERE active= true AND patient_id = '{0}' AND created_at BETWEEN '{1} 00:00:00' AND '{2} 23:59:59' ORDER BY created_at DESC".format(
                        patient_id,initial_date,end_date
                    )
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = MeasurementsFallDetector(
                        row[0], row[1], row[2], row[3]
                    )
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_measurements_location_by_patient(self, patient_id,initial_date,end_date):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT latitude,longitude,id,created_at FROM location WHERE active= true AND patient_id = '{0}' AND created_at BETWEEN '{1} 00:00:00' AND '{2} 23:59:59' ORDER BY created_at DESC".format(
                        patient_id,initial_date,end_date
                    )
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    measurement = LocationPatient(
                        row[0], row[1], row[2], row[3]
                    )
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_measurements_fall_detector_add(self, fallDetectorData):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO fall_detector (description,patient_id)
                                VALUES (%s,%s)""",
                    (fallDetectorData.description, fallDetectorData.patient_id),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_locations_by_date(self, startDate, finalDate):
        try:
            connection = get_connection()
            measurements = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT patient_id,latitude,longitude,(EXTRACT (epoch FROM max(created_at)) *1000)+21600000 AS time FROM location WHERE active=true AND created_at BETWEEN '{0} 00:00:00' AND '{1} 23:59:59' GROUP BY 1,2,3,created_at".format(
                        startDate,finalDate
                    )
                )
                resultset = cursor.fetchall()
                for row in resultset:
                    measurement = Location(
                        row[0], row[1], row[2], row[3]
                    )
                    measurements.append(measurement.to_JSON())

            connection.close()
            return measurements
        except Exception as ex:
            raise Exception(ex)
