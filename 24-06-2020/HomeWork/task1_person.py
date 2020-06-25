"""Создайте класс ПЕРСОНА с абстрактными методами, позволяющими
вывести на экран информацию о персоне, а также определить ее возраст (в
текущем году). Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата
рождения, факультет), СТУДЕНТ (фамилия, дата рождения, факультет, курс),
ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
со своими методами вывода информации на экран и определения возраста.
Создайте список из n персон, выведите полную информацию из базы на
экран, а также организуйте поиск персон, чей возраст попадает в заданный
диапазон."""

from abc import ABC, abstractmethod
from datetime import datetime

class Person(ABC):
    def __init__(self,  second_name, dob, faculty):
        self._second_name = second_name
        self._dob = dob
        self._faculty = faculty

    @abstractmethod
    def __str__(self):
         return f'Second name:\t{self._second_name} \nDate of Birth:\t{self._dob}\nFaculty:\t\t{self._faculty}'

    @abstractmethod
    def age(self):
        today = datetime.now()
        dob = datetime.strptime(self._dob, "%d-%m-%Y")
        age = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1
        return age


class Enrollee(Person):
    def __str__(self):
        result_super = super().__str__()
        return f'\nEnrollee\n{result_super}'

    @property
    def age(self):
        return super().age()

class Student(Person):
    def __init__(self, second_name, dob, faculty, course):
        super().__init__(second_name, dob, faculty)
        self._course = course

    def __str__(self):
        result_super = super().__str__()
        return f'\nStudent\n{result_super}\nCourse:\t\t\t{self._course}'

    @property
    def age(self):
        return super().age()


class Teacher(Person):
    def __init__(self, second_name, dob, faculty, position, experience):
        super().__init__(second_name, dob, faculty)
        self._position = position
        self._experience = experience

    def __str__(self):
        result_super = super().__str__()
        return f'\nTeacher\n{result_super}\nPosition:\t\t{self._position}\nExperience:\t\t{self._experience}'

    @property
    def age(self):
        return super().age()

if __name__ == '__main__':
    persons = [Enrollee('Ivanov', '16-07-2005', 'Journalism'),
               Student('Kozak', '12-04-2001', 'Stinks', 4),
               Teacher('Topol', '01-01-1970', 'Journalism', 'Professor', '25'),
               Student('Kurna', '18-08-1999', 'Stinks', 5)]

    for person in persons:
        print(person)
        print(f'Age:\t\t\t{person.age}')

    print('*'*20)
    print('Filter')
    max_age = 30
    min_age = 17
    for person in filter(lambda person: min_age <= person.age <= max_age, persons):
        print(person)
        print(f'Age:\t\t\t{person.age}')



