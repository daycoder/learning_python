# Read classes_explainer first.

class Person:

    def __init__(self,
                 forename,
                 surname,
                 dob=None,):
        self.forename = forename
        self.surname = surname
        # Store date of birth in a private instance variable (start with __)
        self.__dob = dob

    def __repr__(self):
        return f'Person(forename="{self.forename}", surname="{self.surname}", dob="{self.__dob}")'

    def get_dob(self):  # Don't write getters like this!
        return self.__dob

    @property  # Use a property decorator instead of writing a getter!
    def dob(self):
        return f"I'm sorry I can't do that"

    @dob.setter
    def dob(self, new_dob):
        # This is an overly simple example.
        # Typically you'd use a setter for validation etc
        print('WARNING! Are you using a time machine?')
        self.__dob = new_dob


def main():
    dave = Person(forename="David", surname="King", dob="30/01/1975")

    print(dave)

    # Homework: Look for other decorators people have written, e.g. Add some logging to a function

    dave.forename = 'Dave'
    dave.dob = "30/03/2000"
    ...


brian = Person('Brian', 'Spud', ' 21/01/1898')
if __name__ == "__main__":

    main()