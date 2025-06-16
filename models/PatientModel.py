from werkzeug.security import check_password_hash as checkph

from database.db import get_connection
from .entities.Patient import Patient, Patients, DetailPatient


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
        
    @classmethod
    def get_detail_patient(self,id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT p.id, CONCAT(p.first_name,' ',p.middle_name, '', p.last_name) as full_name_patient,
p.date_of_birth,
CONCAT(ut.first_name,' ',ut.middle_name, '', ut.last_name) as full_name_tutor,
CONCAT(um.first_name,' ',um.middle_name, '', um.last_name) as full_name_doctor,
pgs.general_condition,
pgs.energy,
pgs.fever,
pgs.chest_pain,
pgs.dizziness,
pgs.high_temperature,
pgs.sweating,
pgs.palpitations,
pgs.resting_tachycardia,
pgs.falls,
pgs.instability,
pgs.change_of_location,
pgs.exercise_difficulty,
pgs.dyspnea_activities,
phb.fruits_vegetables,
phb.water,
phb.physical_activity,
phb.sleep_hours,
phb.nighttime_waking,
phb.medical_history,
phb.medications,
phb.cardiac_history,
phb.respiratory_history,
phb.obesity,
phb.family_diabetes,
phb.diabetes,
phb.chronic_disease,
phb.disease_details
FROM patients p 
INNER JOIN users ut ON ut.id = p.tutor_id
INNER JOIN users um ON um.id = p.doctor_id
INNER JOIN patient_general_status pgs ON pgs.patient_id = p.id
INNER JOIN patient_habits_and_backgrounds phb ON phb.patient_id = p.id
WHERE p.active=true and p.id = '{0}'
                    """.format(
                        id
                    )
                )
                row = cursor.fetchone()

                patient = None
                if row != None:
                    patient = DetailPatient(row[0], row[1], row[2], row[3], row[4], row[5],
                            row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]
                            , row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21]
                            , row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29]
                            , row[30], row[31], row[32])
                    patient = patient.to_JSON()

            connection.close()
            return patient
        except Exception as ex:
            raise Exception(ex)
            