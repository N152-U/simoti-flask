class Patient:
    def __init__(self, id, active=True,  first_name=None, middle_name=None, tutor_id=None, doctor_id=None,date_of_birth=None) -> None:
        self.id = id
        self.active = active
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.tutor_id = tutor_id
        self.doctor_id = doctor_id
        self.date_of_birth = date_of_birth
        

    def to_JSON(self):
        return {
            "id": self.id,
            "active": self.active,
            "firstName": self.first_name,
            "middleName": self.middle_name,
            "lastName": self.last_name,
            "tutor_id": self.tutor_id,
            "doctor_id": self.doctor_id,
            "date_of_birth": self.date_of_birth,
        }

class PatientHabitsAndBackgroud:
    def __init__(self, patient_id, first_name=None, middle_name=None, last_name=None, tutor_id=None, doctor_id=None, date_of_birth=None, active=True, fruits_vegetables=None, water=None, physical_activity=None, sleep_hours=None, nighttime_waking=None, medical_history=None, medications=None, cardiac_history=None, respiratory_history=None, obesity=None, family_diabetes=None, diabetes=None, chronic_disease=None, disease_details=None) -> None:
        self.patient_id = patient_id
        self.fruits_vegetables = fruits_vegetables
        self.water = water
        self.physical_activity = physical_activity
        self.sleep_hours = sleep_hours
        self.nighttime_waking = nighttime_waking
        self.medical_history = medical_history
        self.medications = medications
        self.cardiac_history = cardiac_history
        self.respiratory_history = respiratory_history
        self.obesity = obesity
        self.family_diabetes = family_diabetes
        self.diabetes = diabetes
        self.chronic_disease = chronic_disease
        self.disease_details = disease_details
        

     def to_JSON(self):
        return {
            "patientId": self.patient_id,
            "firstName": self.first_name,
            "middleName": self.middle_name,
            "lastName": self.last_name,
            "tutorId": self.tutor_id,
            "doctorId": self.doctor_id,
            "dateOfBirth": self.date_of_birth,
            "active": self.active,
            "fruitsVegetables": self.fruits_vegetables,
            "water": self.water,
            "physicalActivity": self.physical_activity,
            "sleepHours": self.sleep_hours,
            "nighttimeWaking": self.nighttime_waking,
            "medicalHistory": self.medical_history,
            "medications": self.medications,
            "cardiacHistory": self.cardiac_history,
            "respiratoryHistory": self.respiratory_history,
            "obesity": self.obesity,
            "familyDiabetes": self.family_diabetes,
            "diabetes": self.diabetes,
            "chronicDisease": self.chronic_disease,
            "diseaseDetails": self.disease_details
        }