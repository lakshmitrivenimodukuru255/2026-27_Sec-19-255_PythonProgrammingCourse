try:
    numer = float(input("Enter numerator: "))
    denom = float(input("Enter denominator: "))
    print("Quotient:", numer / denom)
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except ValueError:
    print("Please enter valid numbers.")
