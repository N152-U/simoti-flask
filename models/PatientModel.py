from werkzeug.security import check_password_hash as checkph

from database.db import get_connection
from .entities.Patient import Patient, Patients


class PatientModel:

    @classmethod
    def add_patient(self, patient,patientGeneralStatus, newPatientHabitsAndBackgroud):
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
                
                
                cursor.execute(
                    """INSERT INTO patient_habits_and_backgrounds (patient_id, fruits_vegetables, water, physical_activity, sleep_hours, nighttime_waking, 
                    medical_history, medications, cardiac_history, respiratory_history, obesity, family_diabetes, diabetes, chronic_disease, disease_details) 
                                VALUES (%s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s)""",
                    (
                        patient.id,
                        True if newPatientHabitsAndBackgroud.fruits_vegetables == 1 else False,
                        True if newPatientHabitsAndBackgroud.water == 1 else False,
                        True if newPatientHabitsAndBackgroud.physical_activity == 1 else False,
                        True if newPatientHabitsAndBackgroud.sleep_hours == 1 else False,
                        True if newPatientHabitsAndBackgroud.nighttime_waking == 1 else False,
                        True if newPatientHabitsAndBackgroud.medical_history == 1 else False,
                        True if newPatientHabitsAndBackgroud.medications == 1 else False,
                        True if newPatientHabitsAndBackgroud.cardiac_history == 1 else False,
                        True if newPatientHabitsAndBackgroud.respiratory_history == 1 else False,
                        True if newPatientHabitsAndBackgroud.obesity == 1 else False,
                        True if newPatientHabitsAndBackgroud.family_diabetes == 1 else newPatientHabitsAndBackgroud.family_diabetes,
                        True if newPatientHabitsAndBackgroud.diabetes == 1 else newPatientHabitsAndBackgroud.diabetes,
                        True if newPatientHabitsAndBackgroud.chronic_disease == 1 else False,
                        True if newPatientHabitsAndBackgroud.disease_details == 1 else newPatientHabitsAndBackgroud.disease_details

                    ),
                )
                
                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def get_patients(self):
        try:
            connection = get_connection()

            pats = []

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT P.ID AS patient_id,
                    	P.first_name,
                    	P.middle_name,
                    	P.last_name,
                    	CONCAT (u.first_name, ' ', u.middle_name, ' ', u.last_name) AS tutor,
                    	P.date_of_birth
                    FROM
                    	patients
                    	P JOIN users u ON u.ID = P.tutor_id
                    WHERE
                    	P.active = TRUE"""
                                    )
                resultset = cursor.fetchall()

                for row in resultset:
                    pat = Patients(row[0], row[1], row[2], row[3], row[4], row[5])
                    pats.append(pat.to_JSON())

            connection.close()
            return pats
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_patient(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE patients SET active=false WHERE id = %s", (id,)
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_patient(self,id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT P.ID AS patient_id,
                    	P.first_name,
                    	P.middle_name,
                    	P.last_name,
                    	CONCAT (u.first_name, ' ', u.middle_name, ' ', u.last_name) AS tutor,
                    	P.date_of_birth
                    FROM
                    	patients
                    	P JOIN users u ON u.ID = P.tutor_id
                    WHERE
                    	P.active = TRUE
                    AND p.id = '{0}'
                    """.format(
                        id
                    )
                )
                row = cursor.fetchone()

                patient = None
                if row != None:
                    patient = Patients(row[0], row[1], row[2], row[3], row[4], row[5])
                    patient = patient.to_JSON()

            connection.close()
            return patient
        except Exception as ex:
            raise Exception(ex)
            