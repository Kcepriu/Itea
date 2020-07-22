from  models import Author, Post, Tegs
import mongoengine as me

class Initial_Data:
    text_blogs = [
                {'author_name': 'Тетяна Чорновол',
                 'name': '"Слуга народу" – сервісні послуги для олігархів',
                 'body': 'ЗЕ Рада проголосувала "зелену металургію". Тепер, якщо ви ненароком скрутили в''язи, '
                         'бо наркомани вкрали каналізаційний люк, то знайте – це не даремно, бо це ви постраждали '
                         'за зелену металургію!  "Вишки Бойка" блякнуть на тлі нинішніх схем в енергетиці...',
                'tegs':['рада', 'зелена', 'металургія', 'економіка', 'корупція']},

                {'author_name': 'Олексій Братущак',
                 'name': 'Мільярдер з нетрів". Що не так з продажем "Дніпра"',
                 'body': 'Пораділи успішному продажу на аукціоні готелю "Дніпро"? Знаю, пораділи. Навіть сам Зе '
                         'оперативно ФБ-постік видав. Але от запитанєчко. А хто сьогодні "та сторона"? Хто ті '
                         '"невідомі особи", які виграли аукціон? І тут відповідь не така вже легка...',
                 'tegs': ['готель', 'аукціон', 'корупція']},

                {'author_name': 'Ольга Стефанишина',
                 'name': 'Смертельна ціна бездіяльності МОЗ',
                 'body': 'Двоє дітей померло на Волині через бездіяльність МОЗ. Хворому на торсійну дистонію з Донецька '
                         'терміново необхідна операція, а рятівної системи для нього '
                         'нема – заявили пацієнтські організації...',
                 'tegs': ['хвороба', 'паціент', 'діти']},

                {'author_name': 'Олексій Братущак',
                 'name': '"Слуги" споживають інформаційний шлак Кремля. Кейс "тєлєг"',
                 'body': 'Вийшло дослідження анонімних телеграм-каналів. Вилізли вуха Кремля. І тут кремлівські '
                         '"бачки" прорвало. На автора Любов Величко почалась шалена інформаційна атака...',
                 'tegs': ['політика', 'телеграм']},

                {'author_name': 'Дмитро Тузов',
                 'name': 'Думаючи про Україну, пам''ятай Білорусь',
                 'body': 'В перекладі з диктаторської мови фраза Олександра Лукашенка про те, що "він не тримається за '
                         'президентське крісло" означала лише одне: що Лукашенко зубами вп''явся в це саме крісло й '
                         'готовий бити своїх суперників у прямому значенні цього слова...',
                 'tegs': ['політика', 'президент' ]},

                {'author_name': 'Ігор Луценко',
                 'name': 'Законопроект 2280 має бути ветовано!',
                 'body': 'Друзі, на правах співголови Антикорупційної ради при міському голові Києва публікую оцінку '
                         'корупційних ризиків законопроекту 2280, котрий зараз знаходиться на підписі у Президента...',
                 'tegs': ['президент', 'корупція']},

                {'author_name': 'Олексій Братущак',
                 'name': 'Пропаганда РФ: У Криму відбувся ще один "референдум" про "воссоединение"',
                 'body': 'Сьомий рік російські медіа переконують, що анексія відбулася у відповідності з суспільними '
                         ' настроями кримчан. Тепер на підтвердження наводять результати ще одного "референдуму", '
                         'який Кремль провів по всій Росії задля обнулення президентських термінів Путіна...',
                 'tegs': ['анексія', 'референдум', 'політика']},

                {'author_name': 'Альона Гетьманчук',
                 'name': 'Зеленський як альтернатива Путіну на пострадянському просторі. Шанс ще є',
                 'body': 'Одним з позитивних ефектів президентства Зеленського могло б стати збільшення привабливості '
                         'України на пострадянському просторі і взагалі в російськомовному світі '
                         '(не плутати з "русским миром")...',
                'tegs': ['президент', 'політика']},

                {'author_name': 'Дмитро Тузов',
                 'name': 'Путінський план ''інкорпорації'' України і як цьому протидіяти ',
                 'body': 'Пропоную послухати "Медіа-клуб" з Андрієм Піонтковським. Пана Піонтковського ми частіше '
                         'представляємо, як російського політолога. Який із зрозумілих причин працює зараз на значній '
                         'відстані від самої  Росії, витримуючи не лише коронавірусну, а й безпекову дистанцію з режимом '
                         'й спецслужбами Путіна...',
                'tegs': ['політолог', 'політика']},

                {'author_name': 'Альона Гетьманчук',
                 'name': 'Дуда так Дуда',
                 'body': 'Ну що ж, знову Анджей Дуда. Можливо для якихось країн світу болісне переобрання Дуди – це новина,'
                         ' в українських владних кабінетах, склалось враження, ніхто особливо іншого варіанту не очікував...',
                'tegs': ['польща', 'президент']}
                ]

    def add_author(self, first_name, sur_name):
        find_author = Author(first_name=first_name, sur_name=sur_name)
        if not find_author.id:
            find_author.save()

        return find_author

    def add_teg(self, teg_name):
        find_teg = Tegs(teg_name=teg_name)

        print(find_teg.id, teg_name)

        if not find_teg.id:
            find_teg.save()

        print(find_teg.id, teg_name)

        return find_teg

    def initial_data(self):
        for item in self.text_blogs:
            # first_name, sur_name = item['author_name'].split()
            #
            # item['author'] = self.add_author(first_name, sur_name)
            # print(item['name'])
            #
            # kwargs=item.copy()
            # kwargs.pop('tegs')
            #
            # new_post = Post.objects.create(**kwargs)

            # new_post = Post.objects.create(name=item['name'], body=item['body'], author=item['author'], author_name=item['author_name'])

            for text_teg in item['tegs']:
                new_teg = self.add_teg(text_teg)


                # new_post.teg.append(teg=new_teg)

            # new_post.save()




        # print(Author.objects.count())



initial = Initial_Data()
initial.initial_data()

