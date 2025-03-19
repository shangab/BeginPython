

marks = []

name = input("Student Name?:")

math = input("Math Mark?:")
marks.append(float(math))

english = input("English Mark?:")
marks.append(float(english))

science = input("Science Mark?:")
marks.append(float(science))

history = input("History Mark?:")
marks.append(float(history))

total = sum(marks)
average = total / len(marks)

print("Marks: ", marks)

print("Student Name: %s" % name)
print("Total: %0.2f" % total)
print("Average: %0.2f" % average)

if average >= 50:
    print("Pass")
else:
    print("Fail")
