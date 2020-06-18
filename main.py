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

holden = Student("Holden", "Parker", "@holdenp", cohort_37)
daniel = Student("Daniel", "Fuqua", "@danielf", cohort_39)
trey = Student("Trey", "Suiter", "@treys", cohort_36)
willy = Student("Willy", "Metcalf", "@willym", cohort_37)

steve = Instructor("Steve", "Brownlee", "@coach", cohort_37, "dad jokes")
adam = Instructor("Adam", "Sheaffer", "@adams", cohort_39, "digressing")
mo = Instructor("Mo", "Silvera", "@momoney", cohort_36, "interpretive dance")

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
