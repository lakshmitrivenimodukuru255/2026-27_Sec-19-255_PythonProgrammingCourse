filename = "sample.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
    print(content, end="")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
