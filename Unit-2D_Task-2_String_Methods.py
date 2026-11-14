text = "   Hello, Python World!   "

print("Original:", repr(text))
print("upper():", text.upper())
print("lower():", text.lower())
print("strip():", repr(text.strip()))

words = text.strip().split(", ")
print("split():", words)

joined = "-".join(words)
print("join():", joined)

replaced = text.replace("Python", "Coding")
print("replace():", replaced)

print("find('Python'):", text.find("Python"))
