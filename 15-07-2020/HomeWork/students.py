'''Создать базу данных студентов (ФИО, группа, оценки, куратор
студента, факультет). Описать метод для вывода отличников по
каждому факультету. Описать метод для вывода всех студентов
определенного куратора.'''

import mongoengine as me
from init_data import Ititial_Data as ID

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



if __name__ == '__main__':
    me.connect('test2')

    # 1. Інініціалізація даних !!!!!!!!!!!!!
    # init_data = ID(Items, Faculties, Groups, Curators, Student)
    # init_data.initial_data()

    # 2.  Вивести всіх студентів по куратору
    # for student in Student.student_from_curator('Марина', 'Опришкіна'):
    #     print(student)

    student = Student.objects.aggregate(
                {
                  $group :
                    {
                      _id : "$item",
                      totalSaleAmount: { $sum: { $multiply: [ "$price", "$quantity" ] } }
                    }
                 },
                 // Second Stage
                 {
                   $match: { "totalSaleAmount": { $gte: 100 } }
                 }
              )



    filter(mark_student.average('mark') = 10)
    print(student)
    # Student.objects.aggregate()

    # -------------------------------------------
    # print('-'*5, 'Предмети')
    # for i in Items.objects():
    #     print(i)
    #
    # print('-'*5, 'Факультети')
    # for i in Faculties.objects():
    #     print(i)
    #
    # print('-'*5, 'Групи')
    # for i in Groups.objects():
    #     print(i)
    #
    # print('-'*5, 'Куратори')
    # for i in Curators.objects():
    #     print(i)

    # print('-'*5, 'Студенти')
    # for i in Student.objects():
    #     print(i)
    #     for m in i.mark_student:
    #         print(m.name_item, m.mark)






    # print(Items.objects(name_item__startswith='Матемети'))

    # Student.objects.create(first_name='Сергій', sur_name='Костюченко', faculty='Фішико математичний', group='32', curator='Ананьев Бля')
    #
    # for i in Student.objects(sur_name='Костюченко'):
    #     print(i)

    # print(Student.objects.filter(sur_name='Костюченко'))
    # stud = Student.objects.filter(sur_name='Костюченко')[0]
    # # stud.sur_name = 'Боздуган'
    # # stud.save()
    #
    # stud.mark_student.create(mark=5, name_item='Matematics')
    # stud.save()



    # print(Curators.objects.count())
    # print(Curators.objects[17])

