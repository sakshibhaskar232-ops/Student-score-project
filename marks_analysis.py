import matplotlib.pyplot as plt

def calculate_grade(avg):
    if avg >= 85:
        return "A (Excellent)"
    elif avg >= 70:
        return "B (Good)"
    elif avg >= 50:
        return "C (Average)"
    else:
        return "D (Needs Improvement)"

def analyze_student(name, marks):
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    grade = calculate_grade(average)

    print(f"\nReport for {name}")
    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Grade:", grade)

    if average < 60:
        print("Feedback: Needs more focus and consistency.")
    else:
        print("Feedback: Good performance, keep improving!")

    return average

# Example data
student_data = {
    "Aman": [78, 82, 75],
    "Riya": [90, 88, 92],
    "Karan": [60, 65, 58]
}

averages = []

for student, marks in student_data.items():
    avg = analyze_student(student, marks)
    averages.append(avg)

# Visualization
plt.bar(student_data.keys(), averages)
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()
