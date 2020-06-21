from nssPerson import NSSPerson


class Instructor(NSSPerson):
    def __init__(self, specialty):
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)
