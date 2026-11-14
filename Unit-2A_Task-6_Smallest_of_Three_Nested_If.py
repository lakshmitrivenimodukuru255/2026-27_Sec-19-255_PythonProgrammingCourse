num1 = 10
num2 = 25
num3 = 15

if num1 <= num2:
    if num1 <= num3:
        smallest = num1
    else:
        smallest = num3
else:
    if num2 <= num3:
        smallest = num2
    else:
        smallest = num3

print(f"The smallest number is: {smallest}")
