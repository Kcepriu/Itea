import random
import mongoengine as me
from  download_peoples import DownloadPeoples as DP

class Ititial_Data:

    list_item = ['Історія', 'Філософія', 'Психологія', 'Історія', 'Педагогіка']
    list_faculties = ['Філологічний', 'Психологічний', 'Психологічний', 'Педагогічний']
    list_groups = ['11', '12', '21', '22', '31', '32', '41', '42', '51', '52']
    list_curators = [('Архієреєв', 'Сергій'), ('Бабіч', 'Інна'), ('Брік', 'Світлана' ), ('Горкунов', 'Борис' ),
                     ('Демидов', 'Ігор' ), ('Колісник', 'Марія'), ('Маслак', 'Марія'), ( 'Опришкіна', 'Марина' ),
                     ('Скворчевський', 'Олександр' ), ('Чернобровкіна', 'Світлана')]

    def __init__(self, DocumentItem, DocumentFaculties, DocumentGroups, DocumentCurators, DocumentStudent):
        self._DocumentItem = DocumentItem
        self._DocumentFaculties = DocumentFaculties
        self._DocumentGroups = DocumentGroups
        self._DocumentCurators = DocumentCurators
        self._DocumentStudent = DocumentStudent


    def _init_item(self):
        for item in self.list_item:
            try:
                self._DocumentItem.objects.create(name_item=item)
            except me.errors.NotUniqueError:
                pass

    def _init_faculties(self):
        for item in self.list_faculties:
            try:
                self._DocumentFaculties.objects.create(name_faculty=item)
            except me.errors.NotUniqueError:
                pass

    def _init_groups(self):
        for item in self.list_groups:
            try:
                self._DocumentGroups.objects.create(name_group=item)
            except me.errors.NotUniqueError:
                pass

    def _init_curators(self):
        if self._DocumentCurators.objects.count()>5:
            return

        for item in self.list_curators:
            try:
                self._DocumentCurators.objects.create(first_name = item[1], sur_name =item[0] )
            except me.errors.NotUniqueError:
                pass

    def _init_students(self):
        pd = DP()
        list_peoples = pd.get_peoples()

        count_item = self._DocumentItem.objects.count()
        count_faculty = self._DocumentFaculties.objects.count()
        count_group = self._DocumentGroups.objects.count()
        curator_curator = self._DocumentCurators.objects.count()


        i = 0
        while i < 100:
            people = list_peoples[random.randint(1, len(list_peoples))-1]

            try:
                first_name, sur_name = people.split()
            except ValueError:
                continue

            i += 1

            faculty =  self._DocumentFaculties.objects[random.randint(1, count_faculty)-1]
            group = self._DocumentGroups.objects[random.randint(1, count_group)-1]
            curator = self._DocumentCurators.objects[random.randint(1, curator_curator)-1]

            stud = self._DocumentStudent.objects.create(first_name=first_name, sur_name=sur_name,
                                                        faculty=faculty.name_faculty, id_faculty=faculty,
                                                        group=group.name_group, id_group=group,
                                                        curator=curator.__str__(), id_curator=curator)

            for num_mark in range(random.randint(10, 20)):
                item = self._DocumentItem.objects[random.randint(1, count_item)-1]
                mark = random.randint(1 if i % 5 else 10, 12)
                stud.mark_student.create(mark=mark, name_item=item.name_item, id_item=item)

            stud.save()


    def initial_data(self):
        self._init_item()
        self._init_faculties()
        self._init_groups()
        self._init_curators()
        self._init_students()

