rows = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol to print: ")

for i in range(rows, 0, -1):
    print(symbol * i)
