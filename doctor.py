from person import Person

class Doctor(Person):
    def __init__(self, id, specialty, first_name, last_name, ssn):
        super().__init__(first_name, last_name, ssn)
        self.id = id
        self.specialty = specialty

    def get_id(self):
        return self.id

    def get_specialty(self):
        return self.specialty