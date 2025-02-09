class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задание: {self.average_rating}\n' \
              f'Курсы в процессе изучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректное сравнение')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректное сравнение')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

some_lecturer_1 = Lecturer('Наум', 'Львович')
some_lecturer_1.courses_attached += ['Python']

some_lecturer_2 = Lecturer('Николай', 'Матвеев')
some_lecturer_2.courses_attached += ['Java']

some_lecturer_3 = Lecturer('Юрий', 'Решетов')
some_lecturer_3.courses_attached += ['Python']

some_reviewer_1 = Reviewer('Тимур', 'Загитов')
some_reviewer_1.courses_attached += ['Python']
some_reviewer_1.courses_attached += ['Java']

some_reviewer_2 = Reviewer('Оскар', 'Синицын')
some_reviewer_2.courses_attached += ['Python']
some_reviewer_2.courses_attached += ['Java']

some_student_1 = Student('Василий', 'Плошкин')
some_student_1.courses_in_progress += ['Python']
some_student_1.finished_courses += ['Введение в программирование']

some_student_2 = Student('Петр', 'Петров')
some_student_2.courses_in_progress += ['Java']
some_student_2.finished_courses += ['Введение в программирование']

some_student_3 = Student('Иван', 'Иванов')
some_student_3.courses_in_progress += ['Python']
some_student_3.finished_courses += ['Введение в программирование']

some_student_1.rate_hw(some_lecturer_1, 'Python', 10)
some_student_1.rate_hw(some_lecturer_1, 'Python', 10)
some_student_1.rate_hw(some_lecturer_1, 'Python', 10)

some_student_1.rate_hw(some_lecturer_2, 'Python', 5)
some_student_1.rate_hw(some_lecturer_2, 'Python', 7)
some_student_1.rate_hw(some_lecturer_2, 'Python', 8)

some_student_1.rate_hw(some_lecturer_1, 'Python', 7)
some_student_1.rate_hw(some_lecturer_1, 'Python', 8)
some_student_1.rate_hw(some_lecturer_1, 'Python', 9)

some_student_2.rate_hw(some_lecturer_2, 'Java', 10)
some_student_2.rate_hw(some_lecturer_2, 'Java', 8)
some_student_2.rate_hw(some_lecturer_2, 'Java', 9)

some_student_3.rate_hw(some_lecturer_3, 'Python', 5)
some_student_3.rate_hw(some_lecturer_3, 'Python', 6)
some_student_3.rate_hw(some_lecturer_3, 'Python', 7)

some_reviewer_1.rate_hw(some_student_1, 'Python', 8)
some_reviewer_1.rate_hw(some_student_1, 'Python', 9)
some_reviewer_1.rate_hw(some_student_1, 'Python', 10)

some_reviewer_2.rate_hw(some_student_2, 'Java', 8)
some_reviewer_2.rate_hw(some_student_2, 'Java', 7)
some_reviewer_2.rate_hw(some_student_2, 'Java', 9)

some_reviewer_2.rate_hw(some_student_3, 'Python', 8)
some_reviewer_2.rate_hw(some_student_3, 'Python', 7)
some_reviewer_2.rate_hw(some_student_3, 'Python', 9)
some_reviewer_2.rate_hw(some_student_3, 'Python', 8)
some_reviewer_2.rate_hw(some_student_3, 'Python', 7)
some_reviewer_2.rate_hw(some_student_3, 'Python', 9)

print(f'СТУДЕНТЫ:\n\n{some_student_1}\n\n{some_student_2}\n\n{some_student_3}')
print()
print()

print(f'ЛЕКТОРЫ:\n\n{some_lecturer_1}\n\n{some_lecturer_2}\n\n{some_lecturer_3}')
print()
print()

print(f'СРАВНЕНИЕ СТУДЕНТОВ (по средним оценкам за ДЗ): '
      f'{some_student_1.name} {some_student_1.surname} < {some_student_2.name} {some_student_2.surname} = {some_student_1 > some_student_2}')
print()

print(f'СРАВНЕНИЕ ЛЕКТОРОВ (по средним оценкам за лекции): '
      f'{some_lecturer_1.name} {some_lecturer_1.surname} < {some_lecturer_2.name} {some_lecturer_2.surname} = {some_lecturer_1 > some_lecturer_2}')
print()

student_list = [some_student_1, some_student_2, some_student_3]

lecturer_list = [some_lecturer_1, some_lecturer_2, some_lecturer_3]


def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"СРЕДНЯЯ ОЦЕНКА ДЛЯ ВСЕХ СТУДЕНТОВ ПО КУРСУ {'Python'}: {student_rating(student_list, 'Python')}")
print()

print(f"СРЕДНЯЯ ОЦЕНКА ДЛЯ ВСЕХ ЛЕКТОРОВ ПО КУРСУ {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()