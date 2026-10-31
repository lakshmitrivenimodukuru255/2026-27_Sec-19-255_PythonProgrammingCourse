principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in %): "))
time = float(input("Enter time (in years): "))
n = int(input("Enter compounding frequency per year: "))

amount = principal * (1 + (rate / (100 * n))) ** (n * time)
compound_interest = amount - principal

print(f"Total Amount: ₹{amount:.2f}")
print(f"Compound Interest: ₹{compound_interest:.2f}")
