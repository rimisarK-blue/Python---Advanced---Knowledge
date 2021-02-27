
students = int(input())

student_grades = {}

for i in range(students):
    student, grade = input().split(' ')
    grade = float(grade)
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(grade)

for student, grade in student_grades.items():
    average_grade = sum(grade) / len(grade)
    grade = ' '.join(map(lambda x: f'{x:.2f}', grade))

    print(f"{student} -> {grade} (avg: {average_grade:.2f})")