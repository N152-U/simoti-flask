class Patient:
    def __init__(self, id, active=True,  first_name=None, middle_name=None, last_name=None, tutor_id=None, doctor_id=None,date_of_birth=None) -> None:
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
            "tutorId": self.tutor_id,
            "doctorId": self.doctor_id,
            "dateOfBirth": self.date_of_birth,
        }
        
class PatientGeneralStatus:
    def __init__(self, patient_id, general_condition=None, energy=None, fever=None, chest_pain=None, dizziness=None, high_temperature=None, sweating=None, 
                 palpitations=None, resting_tachycardia=None, falls=None, instability=None, change_of_location=None, exercise_difficulty=None, dyspnea_activities=None) -> None:
        self.patient_id = patient_id
        self.general_condition = general_condition
        self.energy = energy
        self.fever = fever
        self.chest_pain = chest_pain
        self.dizziness = dizziness
        self.high_temperature = high_temperature
        self.sweating = sweating
        self.palpitations = palpitations
        self.resting_tachycardia = resting_tachycardia
        self.falls = falls
        self.instability = instability
        self.change_of_location = change_of_location
        self.exercise_difficulty = exercise_difficulty
        self.dyspnea_activities = dyspnea_activities
        

    def to_JSON(self):
        return {
            "patientId": self.patient_id,
            "generalCondition": self.general_condition,
            "energy": self.energy,
            "fever": self.fever,
            "chestPain": self.chest_pain,
            "dizziness": self.dizziness,
            "highTemperature": self.high_temperature,
            "sweating": self.sweating,
            "palpitations": self.palpitations,
            "restingTachycardia": self.resting_tachycardia,
            "falls": self.falls,
            "instability": self.instability,
            "changeOfLocation": self.change_of_location,
            "exerciseDifficulty": self.exercise_difficulty,
            "dyspneaActivities": self.dyspnea_activities
        }

class PatientHabitsAndBackgroud:
    def __init__(self, patient_id, fruits_vegetables=None, water=None, physical_activity=None, sleep_hours=None, nighttime_waking=None, medical_history=None,
                 medications=None, cardiac_history=None, respiratory_history=None, obesity=None, family_diabetes=None, diabetes=None, chronic_disease=None, disease_details=None) -> None:
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