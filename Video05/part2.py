from pybegcor import subjects as subs, students as stds

stdsList = stds.copy()
subsList = subs.copy()


def getGradesAndTotal(marks: list[float]):
    grades = []
    total = 0
    for mark in marks:
        if mark >= 90:
            grades.append("A+")
        elif mark >= 80:
            grades.append("A")
        elif mark >= 70:
            grades.append("B")
        elif mark >= 50:
            grades.append("C")
        else:
            grades.append("F")

        total += mark
    return grades, total


def printCertificate(std):
    std["grades"], std["total"] = getGradesAndTotal(std["marks"])
    print("----------------------------------------------------------")
    print("Certifcate for Stdent :", std["name"])
    print("----------------------------------------------------------")
    print(f"{'SUBJECT':<30} Mark/Grade")

    for i in range(len(subs)):
        print(f"{subs[i]:<30} {std["marks"][i]}/{std["grades"][i]}")
    print("")
    print("----------------------------------------------------------")
    print(f"{'TOTAL':<30} {std["total"]:<30}")
    print("----------------------------------------------------------")


def printSchoolCertificates():
    """Scans all students in the school and prints the certificate of each student.\n
    @params : no paramapaters
    """
    for std in stdsList:
        printCertificate(std)


printSchoolCertificates()
