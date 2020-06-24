class AlreadyExists(Exception):
    pass
class Singletone:

    _instance = None
    #Викликається при створенні обʼєкту до __init__
    def __new__(cls, *args, **kwargs):
        # cls == Singletone
        if cls._instance:
            raise AlreadyExists(f'Object of {cls} already exist')
            #return cls._instance


        obj = super().__new__(cls)
        cls._instance = obj
        #print(obj)
        return obj


    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


obj = Singletone('name')

obj1 = Singletone('new name1')
obj2 = Singletone('new name2')
print(obj.get_name(), obj1.get_name(), obj2.get_name())