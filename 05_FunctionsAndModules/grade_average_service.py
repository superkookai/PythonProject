
def calculate_homework(hw_assignment_grades):
    sum_grades = 0
    for grade in hw_assignment_grades.values():
        sum_grades += grade
    final_grade = round(sum_grades / len(hw_assignment_grades),2)
    print(f"Final Grade: {final_grade}")