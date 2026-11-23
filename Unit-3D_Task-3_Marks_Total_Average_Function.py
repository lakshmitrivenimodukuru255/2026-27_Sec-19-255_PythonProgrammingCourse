def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

total, avg = calculate_marks(80, 90, 85)
print("Total:", total)
print("Average:", avg)
