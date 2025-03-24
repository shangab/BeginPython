from pybegcor import students as stds, subjects as subs

stdsList = stds.copy()
subsList = subs.copy()


class Student:
    def __init__(self, data):
        self.data = data
        self.calculateGradesAndTotal()

    def name(self):
        return self.data["name"]

    def marks(self):
        return self.data["marks"]

    def grades(self):
        return self.data["grades"]

    def total(self):
        return self.data["total"]

    def calculateGradesAndTotal(self):
        self.data["grades"] = []
        self.data["total"] = 0
        for mark in self.data["marks"]:
            if mark >= 90:
                self.data["grades"].append("A+")
            elif mark >= 80:
                self.data["grades"].append("A")
            elif mark >= 70:
                self.data["grades"].append("B")
            elif mark >= 50:
                self.data["grades"].append("C")
            else:
                self.data["grades"].append("F")

            self.data["total"] += mark


class School:
    def __init__(self, students):
        self.students: list[Student] = []
        for std in students:
            self.students.append(Student(std))

    def printCertificates(self):
        for std in self.students:
            print("----------------------------------------------------------")
            print("Certifcate for Stdent :", std.name())
            print("----------------------------------------------------------")
            print(f"{'SUBJECT':<30} Mark/Grade")

            for i in range(len(subs)):
                print(f"{subs[i]:<30} {std.marks()[i]}/{std.grades()[i]}")
            print("")
            print("----------------------------------------------------------")
            print(f"{'TOTAL':<30} {std.total():<30}")
            print("----------------------------------------------------------")


school = School(stdsList)
school.printCertificates()
