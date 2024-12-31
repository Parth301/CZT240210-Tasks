students = {}

def add_student(name, age, grades):
    students[name] = {'Age': age, 'Grades': grades}

def view_student(name):
    return students.get(name, "Student not found.")

def update_student(name, age=None, grades=None):
    if name in students:
        if age:
            students[name]['Age'] = age
        if grades:
            students[name]['Grades'] = grades
    else:
        return "Student not found."

def delete_student(name):
    return students.pop(name, "Student not found.")

add_student("Alice", 20, [90, 85, 88])
print(view_student("Alice"))
update_student("Alice", grades=[95, 92])
print(view_student("Alice"))
delete_student("Alice")
print(view_student("Alice"))
