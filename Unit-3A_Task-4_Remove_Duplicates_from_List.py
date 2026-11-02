data = [1, 2, 2, 3, 1, 4, 3]
unique = []

for i in data:
  if i not in unique:  # Changed 'for' to 'if'
    unique.append(i)

print("original:", data)
print("without duplicates:", unique)
