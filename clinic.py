from person import Person

class Patient(Person):
    pass
class NoSuchPatient(Exception):
    pass

class NoSuchDoctor(Exception):
    pass

class Clinic:
    def __init__(self):
        self.patients = {}
        self.doctors = {}

    def add_patient(self, patient):
        self.patients[patient.get_ssn()] = patient

    def get_patient(self, ssn):
        if ssn not in self.patients:
            raise NoSuchPatient()
        return self.patients[ssn]

    def add_doctor(self, doctor):
        self.doctors[doctor.get_id()] = doctor

    def get_doctor(self, id):
        if id not in self.doctors:
            raise NoSuchDoctor()
        return self.doctors[id]

    def assign_patient_to_doctor(self, patient_ssn, doctor_id):
        patient = self.get_patient(patient_ssn)
        doctor = self.get_doctor(doctor_id)

        patient.set_doctor(doctor)
        doctor.add_patient(patient)

    def idle_doctors(self):
        idle_doctors = []
        for doctor in self.doctors.values():
            if len(doctor.get_patients()) == 0:
                idle_doctors.append(doctor)

        idle_doctors.sort(key=lambda doctor: (doctor.get_last_name(), doctor.get_first_name()))
        return idle_doctors

    def busy_doctors(self):
        average_num_patients = len(self.patients) / len(self.doctors)

        busy_doctors = []
        for doctor in self.doctors.values():
            if len(doctor.get_patients()) > average_num_patients:
                busy_doctors.append(doctor)

        busy_doctors.sort(key=lambda doctor: (doctor.get_last_name(), doctor.get_first_name()))
        print(busy_doctors)

    def doctors_by_num_patients(self):
        doctors_by_num_patients = []
        for doctor in self.doctors.values():
            num_patients = len(doctor.get_patients())
            doctors_by_num_patients.append(f"{num_patients:d}: {doctor.get_last_name()} {doctor.get_first_name()}")

        doctors_by_num_patients.sort(key=lambda doctor: (doctor.split(":")[0], doctor.split(":")[1]))
        print(doctors_by_num_patients)

    def count_patients_per_specialization(self):
        count_patients_per_specialization = {}
        for doctor in self.doctors.values():
            specialty = doctor.get_specialty()
            if specialty not in count_patients_per_specialization:
                count_patients_per_specialization[specialty] = 0

            count_patients_per_specialization[specialty] += len(doctor.get_patients())

        list_count_patients_per_specialization = []
        for specialty, count_patients in count_patients_per_specialization.items():
            list_count_patients_per_specialization.append(f"{count_patients:d} - {specialty}")

        list_count_patients_per_specialization.sort(key=lambda count_patients: (count_patients.split("-")[1], count_patients.split))
