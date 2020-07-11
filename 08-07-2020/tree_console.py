class Command:
    def __init__(self, text, func, tree):
        self.tree = tree


class TreeConsole:
    def __init__(self):
        tree_1 = {'1': ('Авторизироватся', (lambda ss: ss.active_tree = TreeConsole().tree_2)),
                  'q': ('Выход', '')}

        tree_2 = {'1': ('Администрирование', ''),
                  '2': ('Работа с данными', ''),
                  'q': ('Выход', '')
                  }
        tree = {'1':{'text':'Авторизация',
                     'command':'func',
                    }
                'q':''}
        self.running = True
        self.active_tree = tree_1

    def run(self):
        while True:
            self.print_command(self.active_tree)

            command = input('Ведите команду: ')
            if command == 'q':
                break
            elif command in self.active_tree:
                print(self.active_tree[command][0])
                self.active_tree[command][1](self)
            else  :
                print('Не верная комманда')

    def print_command(self, tree):
        for i in tree:
            print(i, f" - {tree[i][0]}")

if __name__ == '__main__':
    console = TreeConsole()
    console.run()
