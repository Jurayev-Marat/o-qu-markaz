class User:
    def __init__(self, name, username, role):
        self.name = name
        self.username = username
        self.role = role

    def login(self, username, password):
        return self.username == username and password == username


class Student(User):
    def __init__(self, name, username, phone):
        super().__init__(name, username, 'student')
        self.phone = phone
        self.homeworks = []
        self.grades = []
        self.group = None

    def view_homeworks(self):
        if not self.homeworks:
            print("Sizga hali uyga vazifa berilmagan.")
        else:
            print("Uyga vazifalar:")
            for hw in self.homeworks:
                print(f"- {hw}")

    def view_grades(self):
        if not self.grades:
            print("Sizga hali baho qo‘yilmagan.")
        else:
            print("Baholar:")
            for grade in self.grades:
                print(f"- {grade}")


class Teacher(User):
    def __init__(self, name, username, phone):
        super().__init__(name, username, 'teacher')
        self.phone = phone
        self.groups = []

    def assign_homework(self, homework, students):
        for student in students:
            student.homeworks.append(homework)
        print("Uyga vazifa berildi.")

    def grade_student(self, student_name, grade, students):
        for student in students:
            if student.name == student_name:
                student.grades.append(grade)
                print(f"{student_name} ga {grade} baho qo‘yildi.")
                return
        print("O‘quvchi topilmadi.")

    def view_group(self, group_name, students):
        group_students = [s for s in students if s.group == group_name]
        print(f"Guruh '{group_name}' o‘quvchilari:")
        for student in group_students:
            print(f"- {student.name}")


class Admin(User):
    def __init__(self, name='Admin', username='admin'):
        super().__init__(name, username, 'admin')
        self.groups = {}

    def add_teacher(self, name, username, phone):
        teacher = Teacher(name, username, phone)
        print(f"O‘qituvchi '{name}' qo‘shildi.")
        return teacher

    def add_student(self, name, username, phone):
        student = Student(name, username, phone)
        print(f"O‘quvchi '{name}' qo‘shildi.")
        return student

    def create_group(self, group_name, teacher_username, teachers):
        if group_name in self.groups:
            print("Bunday guruh mavjud.")
            return False
        for t in teachers:
            if t.username == teacher_username:
                self.groups[group_name] = teacher_username
                t.groups.append(group_name)
                print(f"Guruh '{group_name}' yaratildi va '{t.name}'ga biriktirildi.")
                return True
        print("O'qituvchi topilmadi.")
        return False

    def add_student_to_group(self, student_username, group_name, students):
        for s in students:
            if s.username == student_username:
                s.group = group_name
                print(f"{s.name} guruh '{group_name}' ga qo‘shildi.")
                return True
        print("O‘quvchi topilmadi.")
        return False

    def remove_student_from_group(self, student_username, students):
        for s in students:
            if s.username == student_username:
                if s.group:
                    print(f"{s.name} guruh '{s.group}' dan chiqarildi.")
                    s.group = None
                    return True
                else:
                    print("O‘quvchi guruhda yo‘q.")
                    return False
        print("O‘quvchi topilmadi.")
        return False