from pybegcor import students as stds

# newList = []

# for std in stds:
#     if std["class"] == 6:
#         newList.append(std.copy())


# newList = [std.copy() for std in stds if std["class"] == 6]

nums = [1, 5, 6, 4, 18, 23, 77, 90, 11]
newList = [x for x in nums if x % 2 == 1]
print(newList)
