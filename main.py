from clinic import Clinic, NoSuchDoctor, NoSuchPatient
from person import Person
from doctor import Doctor


clinic = Clinic()

patient1 = Person("Erkinboyev", "G'olibjon", "123-45-6789")
patient2 = Person("Karimov", "Islom", "987-65-4321")

clinic.add_patient(patient1)
clinic.add_patient(patient2)

doctor1 = Doctor("Dr.Qudratov", "Ravshan", "111-22-3333", "D12345", "Cardiolog")
doctor2 = Doctor("Dr.Akramov", "Sherzod", "444-55-6666", "D67890", "Pediatr")

clinic.add_doctor(doctor1)
clinic.add_doctor(doctor2)




try:
    patient = clinic.get_patient("123-45-6789")
    print("Bemor:", patient.get_first_name(), patient.get_last_name())
except NoSuchPatient as e:
    print(e)

try:
    doctor = clinic.get_doctor("D12345")
    print("Doctor :", doctor.get_first_name(), doctor.get_last_name())
except NoSuchDoctor as e:
    print(e)

