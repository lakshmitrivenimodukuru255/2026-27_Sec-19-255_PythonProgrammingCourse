
print("Using for loop:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\nUsing while loop:")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
