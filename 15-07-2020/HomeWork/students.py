'''Создать базу данных студентов (ФИО, группа, оценки, куратор
студента, факультет). Описать метод для вывода отличников по
каждому факультету. Описать метод для вывода всех студентов
определенного куратора.'''

import mongoengine as me
from seeder import Ititial_Data as ID

class Items(me.Document):
    name_item = me.StringField(min_length=1, max_length=255, required=True, unique=True)

    def __str__(self):
        return self.name_item


class Faculties(me.Document):
    name_faculty = me.StringField(min_length=1, max_length=255, required=True, unique=True)

    def __str__(self):
        return self.name_faculty


class Groups(me.Document):
    name_group = me.StringField(min_length=1, max_length=255, required=True, unique=True)

    def __str__(self):
        return self.name_group


class Curators(me.Document):
    first_name = me.StringField(min_length=1, max_length=255, required=True)
    sur_name = me.StringField(min_length=1, max_length=255, required=True)

    def __str__(self):
        # return f'First name: {self.first_name} Sur name: {self.sur_name}'
        return f'{self.first_name} {self.sur_name}'


class Mark(me.EmbeddedDocument):
    mark = me.IntField(min_value=1, max_value=12)
    id_item = me.ReferenceField(Items)
    name_item = me.StringField(min_length=1, max_length=255, required=True)


class Student(me.Document):
    first_name = me.StringField(min_length=1, max_length=255, required=True)
    sur_name = me.StringField(min_length=1, max_length=255, required=True)

    faculty = me.StringField(min_length=1, max_length=255, required=True)
    id_faculty = me.ReferenceField(Faculties)

    group = me.StringField(min_length=1, max_length=255, required=True)
    id_group = me.ReferenceField(Groups)

    curator = me.StringField(min_length=1, max_length=255, required=True)
    id_curator = me.ReferenceField(Curators)

    mark_student = me.EmbeddedDocumentListField(Mark)

    def __str__(self):
        return f'{self.sur_name} {self.first_name} студент {self.faculty} факультета, {self.group} групи. ' \
               f'Куратор {self.curator} '

    def str_mark(self):
        result = ''
        for m in self.mark_student:
            result += f('{m.name_item}: {m.mark}')

        return result

    def student_from_curator(first_name, sur_name):
        curators = Curators.objects.filter(first_name=first_name, sur_name=sur_name)
        if curators:
            curator = curators[0]
        else:
            return []

        return Student.objects.filter(id_curator=curator)

    def Excellent_Students_Faculties():
        result = ''
        for faculty in Faculties.objects:
            result += faculty.name_faculty+'\n'
            students = Student.objects(id_faculty=faculty.id).aggregate([
                {'$unwind': '$mark_student'},
                {'$group': {'_id': '$_id', 'average_mark': {'$avg': '$mark_student.mark'}}},
                {'$match': {'average_mark': {'$gte': 10.0}}}
            ])

            for student in students:
                result += f"\t{Student.objects(id=student['_id'])[0].__str__()},  середній бал {round(student['average_mark'], 2)} \n"

        return result

if __name__ == '__main__':
    me.connect('test3')

    # 1. Інініціалізація даних !!!!!!!!!!!!!
    # init_data = ID(Items, Faculties, Groups, Curators, Student)
    # init_data.initial_data()

    # 2.  Вивести всіх студентів по куратору
    for student in Student.student_from_curator('Марина', 'Опришкіна'):
         print(student)

    # 3. Відмінники по факультетам
    print(Student.Excellent_Students_Faculties())

