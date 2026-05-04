# Create a list of dictionaries to store student records

students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}
]

# Print the name of each student

print("Student names:")
for s in students:
    print(s["name"])

# Print the average score

total = 0
for s in students:
    total += s["score"]

avg = total / len(students)
print("\nAverage score:", avg)

# Add a new student

students.append({"id": 104, "name": "John", "score": 75})
print("\nStudent list:", students)

# Update score of student with ID 102

for s in students:
    if s["id"] == 102:
        s["score"] = 88

print("\nUpdated student list:", students)

# Delete student named Charlie

new_list = []
for s in students:
    if s["name"] != "Charlie":
        new_list.append(s)

students = new_list
print("\nAfter deleting Charlie:", students)

# Students who scored more than 80

print("\nStudents scoring more than 80:")
for s in students:
    if s["score"] > 80:
        print(s["name"])

# Sort students by score (descending)

def get_score(student):
    return student["score"]

students.sort(key=get_score, reverse=True)

print("\nSorted by score (descending):")
for s in students:
    print(s)

# Find student with highest score

max_score = max(s["score"] for s in students)

top_student = []
for s in students:
    if s["score"] == max_score:
        top_student.append(s)

print("\nTop student:", top_student)

# Function to assign grade

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

# Student report

print("\nStudent Report:")
for s in students:
    grade = get_grade(s["score"])
    print("Name:", s["name"], "| Score:", s["score"], "| Grade:", grade)

# Count grades

grade_count = {"A": 0, "B": 0, "C": 0}

for s in students:
    grade = get_grade(s["score"])
    grade_count[grade] += 1

print("\nGrade count:", grade_count)
