num = int(input("Enter a 3-digit number: "))
temp = num
sum_cubes = 0

while temp > 0:
    digit = temp % 10
    sum_cubes += digit ** 3
    temp //= 10

if num == sum_cubes:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
