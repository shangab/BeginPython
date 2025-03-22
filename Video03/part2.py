subjects = ["math", "english", "science", "history", "Chem"]
marks = [90, 80, 70, 60, 40]
grades = []
name = "Ahmed Ali"

for idx, _ in enumerate(marks):
    if marks[idx] >= 90:
        grades.append("A+")
    elif marks[idx] >= 80:
        grades.append("A")
    elif marks[idx] >= 70:
        grades.append("B")
    elif marks[idx] >= 50:
        grades.append("C")
    else:
        grades.append("F")

print("--------------------------------------------------------")
print(f"Certificate of : {name}")
print("--------------------------------------------------------")
total = 0
print("SUBJECT\t\t\t\t\t MARK/GRADE")
for index, subject in enumerate(subjects):
    print(f"{subject}\t\t\t\t\t {marks[index]}/{grades[index]}")
    total += marks[index]

print("--------------------------------------------------------")
print(f"Total:\t\t\t\t\t {total}")
print("--------------------------------------------------------")
