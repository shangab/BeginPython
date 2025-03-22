from pybegcor import subjects

# newSubs = subjects.copy()
# newSubs.append("New 1")

# print(subjects)
# print(newSubs)

# newSubs = subjects[:3]
# newSubs.append("New 1")

# print(type(newSubs))

# print(subjects)

newSubs = subjects.copy()
print("Original: ", newSubs)

count = newSubs.count("Math")
print("count items: ", count)

newSubs.reverse()
print("After reverse: ", newSubs)

newSubs.extend(["New1", "New2"])
print("After extending: ", newSubs)

newSubs.reverse()
print("After reverse: ", newSubs)

newSubs.sort()
print("After sort: ", newSubs)

newSubs.pop()
print("After pop(): ", newSubs)
