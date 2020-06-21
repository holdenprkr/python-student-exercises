from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

bank_heist = Exercise("Bank Heist", "CSharp")
martins_aquarium = Exercise("Martin's Aquarium", "JavaScript")
bangazon = Exercise("Bangazon", "Python")
kennels = Exercise("Kennels", "React")

cohort_36 = Cohort("Day Cohort 36")
cohort_37 = Cohort("Day Cohort 37")
cohort_39 = Cohort("Day Cohort 39")

holden = Student()
holden.first_name = "Holden"
holden.last_name = "Parker"
holden.slack_handle = "@holdenp"
holden.cohort = cohort_37
daniel = Student()
daniel.first_name = "Daniel"
daniel.last_name = "Fuqua"
daniel.slack_handle = "@danielf"
daniel.cohort = cohort_39
trey = Student()
trey.first_name = "Trey"
trey.last_name = "Suiter"
trey.slack_handle = "@treys"
trey.cohort = cohort_36
willy = Student()
willy.first_name = "Willy"
willy.last_name = "Metcalf"
willy.slack_handle = "@willym"
willy.cohort = cohort_37

steve = Instructor("dad jokes")
steve.first_name = "Steve"
steve.last_name = "Brownlee"
steve.slack_handle = "@coach"
steve.cohort = cohort_37
adam = Instructor("disgressing")
adam.first_name = "Adam"
adam.last_name = "Sheaffer"
adam.slack_handle = "@adams"
adam.cohort = cohort_39
mo = Instructor("interpretive dance")
mo.first_name = "Mo"
mo.last_name = "Silvera"
mo.slack_handle = "@momoney"
mo.cohort = cohort_36

steve.assign_exercise(holden, martins_aquarium)
steve.assign_exercise(holden, kennels)
steve.assign_exercise(willy, martins_aquarium)
steve.assign_exercise(willy, kennels)
adam.assign_exercise(daniel, bank_heist)
adam.assign_exercise(daniel, bangazon)
mo.assign_exercise(trey, bangazon)
mo.assign_exercise(trey, martins_aquarium)

students = list()
students.append(holden)
students.append(daniel)
students.append(trey)
students.append(willy)

exercises = list()
exercises.append(bank_heist)
exercises.append(martins_aquarium)
exercises.append(bangazon)
exercises.append(kennels)

for student in students:
    report = f"{student.first_name} {student.last_name} is working on "
    for x in range(0, len(student.exercises)):
        if x == len(student.exercises) - 1:
            report += f"and {student.exercises[x].name}."
        else:
            report += f"{student.exercises[x].name}, "

    print(report)
