from werkzeug.security import check_password_hash as checkph

from database.db import get_connection
from .entities.Patient import Patient


class PatientModel:

    @classmethod
    def add_patient(self, patient):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO patients (id, active, first_name, middle_name, last_name, tutor_id, doctor_id, date_of_birth) 
                                VALUES (%s, %s, %s,%s, %s, %s, %s,%s)""",
                    (
                        patient.id,
                        patient.active,
                        patient.first_name,
                        patient.middle_name,
                        patient.last_name,
                        patient.tutor_id,
                        patient.doctor_id,
                        patient.date_of_birth
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)