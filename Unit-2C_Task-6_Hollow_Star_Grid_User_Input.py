n = int(input("Enter the grid size (N): "))

for i in range(n):
    for j in range(n):
        # Print star for boundary rows and columns, otherwise print space
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to the next line after each row
