class Person:
    def __init__(self, first_name, last_name, ssn):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_ssn(self):
        return self.ssn