count = 0

def increase():
    global count
    count = count + 1
    print("Inside function, count:", count)

print("Before:", count)
increase()
print("After:", count)
