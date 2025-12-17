num = 20
output = []
for i in range(1, num+1):
    if i % 3 == 0  and i % 5 == 0:
        output.append("FizzBuzz")
    elif i % 3==0:
        output.append("Fizz")
    elif i % 5==0:
        output.append("Buzz")
    else:
        output.append(str(i))
print(output) 