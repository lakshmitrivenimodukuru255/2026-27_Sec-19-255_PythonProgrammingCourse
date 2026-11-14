
str = input("Enter a string: ")
count = 0
for i in str:
  count += 1

print(f"Total characters: {count}")                     
print(f"Char: {i}, Frequency: {str.count(i)}")
