import matplotlib.pyplot as plt

students = []
marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    score = int(input("Enter marks: "))
    students.append(name)
    marks.append(score)

# Combine and sort
data = list(zip(students, marks))
data.sort(key=lambda x: x[1], reverse=True)

# Display ranking
print("\n--- Student Rankings ---")
for i, (name, score) in enumerate(data, start=1):
    print(f"{i}. {name} - {score}")

# Extract sorted data
sorted_students = [x[0] for x in data]
sorted_marks = [x[1] for x in data]

# Visualization
plt.bar(sorted_students, sorted_marks)
plt.title("Student Ranking System")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
