students = ["Aida", "Dana", "Tom"]
scores = [90, 85, 96]

# enumerate(): get index and value
print("Student list:")
for index, student in enumerate(students, start=1):
    print(index, student)

# zip(): iterate through lists together
print("\nStudents and scores:")
for student, score in zip(students, scores):
    print(f"{student}: {score}")

# zip() stops at the shortest iterable
print("\nPaired values:", list(zip(students, scores)))
