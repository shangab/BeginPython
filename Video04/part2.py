from pybegcor import subjects as subs, students as stds


# Calculate grades
newList = stds.copy()
for std in stds:
    marks = std["marks"]
    std["grades"] = []
    std["total"] = 0
    for mark in marks:
        if mark >= 90:
            std["grades"].append("A+")
        elif mark >= 80:
            std["grades"].append("A")
        elif mark >= 70:
            std["grades"].append("B")
        elif mark >= 50:
            std["grades"].append("C")
        else:
            std["grades"].append("F")
        std["total"] += mark

# Print Certificates

for std in newList:
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
