from person import Person

class Doctor(Person):
    def __init__(self, first_name, last_name, cnn,  id_number, specialty):
        super().__init__(first_name, last_name, cnn )
        self.id_number = id_number
        self.specialty = specialty

    def get_id_number(self):
        return self.id_number

    def get_specialty(self):
        return self.specialty

