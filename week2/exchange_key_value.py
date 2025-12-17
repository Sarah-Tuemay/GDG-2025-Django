grades = {"John": "A", "Sara": "B", "Musa": "A"}

output = {}
# initializing with empty array
for key in grades:
    output[grades[key]] = []

for key in grades:
    output[grades[key]].append(key)
print(output)