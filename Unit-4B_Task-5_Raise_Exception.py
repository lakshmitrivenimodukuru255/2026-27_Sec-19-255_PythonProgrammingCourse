try:
    age = int(input("Enter age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Valid age:", age)
except ValueError as e:
    print("Error:", e)
