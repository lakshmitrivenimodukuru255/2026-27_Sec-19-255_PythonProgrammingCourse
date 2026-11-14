num1 = 10
num2 = 25
num3 = 15

if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

print(f"The largest number is: {largest}")
