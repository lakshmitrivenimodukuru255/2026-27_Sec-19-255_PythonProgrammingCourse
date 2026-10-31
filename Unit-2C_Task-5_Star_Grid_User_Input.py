n = int(input("Enter the grid size (N): "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()  # Moves to the next line after each row
