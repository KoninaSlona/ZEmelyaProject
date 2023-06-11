"""
B этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и ego решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение c сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
a не просто принт 'You are late'.
Поднимайте исключение DeadlineError c сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования c помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура c интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
K названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict

class Homework:
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        current_time = datetime.datetime.now()
        return current_time <= (self.created + self.deadline)


class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')
        if not homework.is_active():
            raise DeadlineError('You are late')
        return HomeworkResult(self, homework, solution)


class Teacher:
    homework_done = defaultdict(set)

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text: str, deadline: int):
        return Homework(text, deadline)

    def check_homework(self, homework_result: 'HomeworkResult'):
        if len(homework_result.solution) > 5:
            self.homework_done[homework_result.homework].add(homework_result)

    @classmethod
    def reset_results(cls, homework=None):
        if homework:
            del cls.homework_done[homework]
        else:
            cls.homework_done.clear()


class HomeworkResult:
    def __init__(self, author: Student, homework: Homework, solution: str):
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


class DeadlineError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    try:
        result_3 = lazy_student.do_homework(docs_hw, 'done')
    except DeadlineError as e:
        print(e)  # You are late

    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except TypeError as e:
        print(e)  # You gave a not Homework object

    opp_teacher.check_homework(result_1)
    print(Teacher.homework_done[oop_hw])

    advanced_python_teacher.check_homework(result_1)
    print(Teacher.homework_done[oop_hw])

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])

    Teacher.reset_results(oop_hw)
    print(Teacher.homework_done)
