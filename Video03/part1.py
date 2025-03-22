# for i in range(5):
#     print(f"Hello, world! {i}")


# i = 0
# while i < 5:
#     print(f"Hello, world! {i}")
#     i += 1

subjects = ["math", "english", "science", "history"]
marks = [90, 80, 70, 60]
name = "Ahmed Ali"

print("-------------------------------")
print(f"Certificate of : {name}")
print("-------------------------------")
total = 0
for index, subject in enumerate(subjects):
    print(f"{subject}\t\t\t\t\t ...{marks[index]}")
    total += marks[index]

print(f"Total:\t\t\t\t\t ...{total}")
