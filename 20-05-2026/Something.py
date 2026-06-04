# Python opp student
# Topic covered

'''
1. Class & Obj
2. Self Keyword
3. Del keyword
4. Encapsulation
'''

# calss and object

class car:
    comp_name = None
    model = None
    color = None
    year = None

car1 = car()
car2 = car()

car1.comp_name = "BMW"
car1.model = "M5"
car1.color = "Black"
car1.year = "2021"

car2.comp_name = "Mercedes"
car2.model = "S Class"
car2.color = "Black"
car2.year = "2023"

print("\nCar 1 Detail")
print(car1.comp_name)
print(car1.model)
print(car1.color)
print(car1.year)

print("\nCar 2 Detail")
print(car2.comp_name)
print(car2.model)
print(car2.color)
print(car2.year)

# Student

class StudentData:
    std_name = None
    std_id = None
    std_age = None
    std_course = None

student1 = StudentData()

student1.std_name = "Rakesh"
student1.std_id = 7045
student1.std_age = 17
student1.std_course = "AI/ML"

print("\nStudent 1 Detail")
print(student1.std_name)
print(student1.std_id)
print(student1.std_age)
print(student1.std_course)
