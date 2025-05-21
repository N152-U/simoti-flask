from werkzeug.security import check_password_hash as checkph

from database.db import get_connection
from .entities.Patient import Patient


class PatientModel:

    @classmethod
    def add_patient(self, patient,patientGeneralStatus):
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
                
                cursor.execute(
                    """INSERT INTO patient_general_status (patient_id, general_condition, energy, fever, chest_pain, dizziness, high_temperature, sweating, 
                 palpitations, resting_tachycardia, falls, instability, change_of_location, exercise_difficulty, dyspnea_activities) 
                                VALUES (%s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s)""",
                    (
                        patient.id,
                        True if patientGeneralStatus.general_condition == 1 else False,
                        True if patientGeneralStatus.energy == 1 else False,
                        True if patientGeneralStatus.fever == 1 else False,
                        True if patientGeneralStatus.chest_pain == 1 else False,
                        True if patientGeneralStatus.dizziness == 1 else False,
                        True if patientGeneralStatus.high_temperature == 1 else False,
                        True if patientGeneralStatus.sweating == 1 else False,
                        True if patientGeneralStatus.palpitations == 1 else False,
                        True if patientGeneralStatus.resting_tachycardia == 1 else False,
                        True if patientGeneralStatus.falls == 1 else False,
                        True if patientGeneralStatus.instability == 1 else False,
                        True if patientGeneralStatus.change_of_location == 1 else False,
                        True if patientGeneralStatus.exercise_difficulty == 1 else False,
                        True if patientGeneralStatus.dyspnea_activities == 1 else False

                    ),
                )
                
                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)