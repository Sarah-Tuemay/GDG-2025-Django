input = "python is fun and python is powerful"
splited = input.split()

output = {}

for word in splited:
    output[word] = 0

for word in splited:
    output[word] += 1
print(output)
