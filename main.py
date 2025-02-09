class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_grades_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_dict_lecturer:
                lecturer.grades_dict_lecturer[course] += [grade]
            else:
                lecturer.grades_dict_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашние задания: {self.grades}\n' f'Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n' f'Завершенные курсы: {','.join(self.finished_courses)}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades_dict_lecturer = {}
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
             if course in student.grades:
                 student.grades[course] += [grade]
             else:
                 student.grades[course] = [grade]
         else:
             return 'Ошибка'



some_reviewer = Reviewer('Иван', 'Иванов')

some_lecturer = Lecturer('Николай', 'Синицын')


some_student = Student('Юрий', 'Григорьев', 'your_gender')

some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_student.add_grades_lecturer(some_student, 'Python', 9.9)

print(some_reviewer)
print(some_lecturer.grades_dict_lecturer)
print(some_student)