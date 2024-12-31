class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", 21, [85, 90, 80])
student.display_details()
print(f"Average Grade: {student.calculate_average()}")
