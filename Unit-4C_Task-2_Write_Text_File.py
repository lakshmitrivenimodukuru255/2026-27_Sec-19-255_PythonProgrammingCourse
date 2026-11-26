filename = "output.txt"
text = "Learning file handling in Python."
try:
  with open(filename, "w") as file:
    file.write(text)
  print("Data written to", filename)
except FileNotFoundError:
  print(f"File'{filename}' not found.")
