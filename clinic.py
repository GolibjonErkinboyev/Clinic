

class Clinic:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def get_patient(self, ssn):
        for patient in self.patients:
            if patient.get_ssn() == ssn:
                return patient
        raise NoSuchPatient("SSN bilan bemor topilmadi: {}".format(ssn))

    def get_doctor(self, id_number):
        for doctor in self.doctors:
            if doctor.get_id_number() == id_number:
                return doctor
        raise NoSuchDoctor("Hech qanday shifokor topilmadi: {}".format(id_number))

class NoSuchPatient(Exception):
    pass

class NoSuchDoctor(Exception):
    pass