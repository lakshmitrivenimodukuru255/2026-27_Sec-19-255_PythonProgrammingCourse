def display_student(name, **marks):
    print(name)
    for subject, score in marks.items():
        print(subject, score)

display_student("Alex", math=90, science=85)
